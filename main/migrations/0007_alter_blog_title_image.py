# Generated by Django 5.1 on 2024-09-11 12:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_blog_content_alter_blog_title_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title_image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dpyxbvcyl/image/upload/v1726002039/Blog/g2dpyp3jmtel9u2kgjvi.jpg', max_length=255, verbose_name='image'),
        ),
    ]
