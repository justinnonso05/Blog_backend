from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from cloudinary.api import cloudinary
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import uuid
import re
from django.core.exceptions import ValidationError
# from django_summernote.fields import SummernoteTextField
# from django_summernote.fields import SummernoteTextField

def validate_no_emoji(value):
    # Regular expression to match most emojis
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & pictographs
        "\U0001F680-\U0001F6FF"  # Transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # Flags (iOS)
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed characters
        "]+",
        flags=re.UNICODE,
    )
    if emoji_pattern.search(value):
        raise ValidationError("Emojis are not allowed in this field.")



class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('entertainment', 'Entertainment'),
        ('opinion_commentaries', 'Opinions & Commentaries'),
        ('sports', 'Sports'),
        ('news-report', 'News Reports'),
        ('bizz_napss', 'BizzNAPSS'),
        ('interviews', 'Interviews'),
        ('articles_essays', 'Articles & Essays'),
        # Add more categories as needed
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, validators=[validate_no_emoji], help_text="No emojis allowed.")
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    title_image = CloudinaryField('image', folder="Blog/title/", default="https://res.cloudinary.com/dpyxbvcyl/image/upload/v1726002039/Blog/g2dpyp3jmtel9u2kgjvi.jpg")
    # title_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    # content = models.TextField()  # Integrating Summernote for rich text content
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        
        # Convert title image to WebP before uploading to Cloudinary
        if self.title_image and hasattr(self.title_image, 'file'):
            self.title_image = self.convert_image_to_webp(self.title_image)

        super().save(*args, **kwargs)

    def convert_image_to_webp(self, image_field):
        # Open the image using Pillow
        img = Image.open(image_field.file)
        
        # Convert to WebP format
        img_io = BytesIO()  # Create an in-memory bytes buffer
        img.save(img_io, format="WEBP", quality=20)  # Save image to buffer as WebP
        
        # Prepare the file for Cloudinary upload
        img_io.seek(0)  # Go to the beginning of the buffer
        content = ContentFile(img_io.read(), name=f"{self.slug}.webp")  # Use slug for naming
        
        # Upload the WebP image to Cloudinary
        upload_result = cloudinary.uploader.upload(content, folder="Blog/title/", secure=True)
        return upload_result['secure_url']  # Return the URL of the uploaded WebP image

    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug
    
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:10]


# def generate_token():
#     return uuid.uuid4().hex

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    unsubscribe_token = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.email
