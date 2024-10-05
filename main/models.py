from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
# from django_summernote.fields import SummernoteTextField
# from django_summernote.fields import SummernoteTextField


class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Tech'),
        ('lifestyle', 'Lifestyle'),
        ('education', 'Education'),
        # Add more categories as needed
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
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
        super().save(*args, **kwargs)

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