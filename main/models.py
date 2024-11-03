from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from cloudinary.api import cloudinary
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# from django_summernote.fields import SummernoteTextField
# from django_summernote.fields import SummernoteTextField


class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Tech'),
        ('lifestyle', 'Lifestyle'),
        ('education', 'Education'),
        ('health', 'Health'),
        # Add more categories as needed
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
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


class Subscriber(models.Model):
    email = models.EmailField()
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
