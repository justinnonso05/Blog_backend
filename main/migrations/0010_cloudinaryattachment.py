# Generated by Django 5.1 on 2024-09-11 18:25

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_blog_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudinaryAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Defaults to filename, if left blank', max_length=255, null=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='file')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
