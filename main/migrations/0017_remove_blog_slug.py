# Generated by Django 5.1 on 2024-09-28 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
