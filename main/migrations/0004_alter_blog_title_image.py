# Generated by Django 5.1 on 2024-09-10 19:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title_image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dpyxbvcyl/image/upload/v1725997470/Blog_images/t30oabfqgl4jr08krfni.jpg', max_length=255, verbose_name='image'),
        ),
    ]
