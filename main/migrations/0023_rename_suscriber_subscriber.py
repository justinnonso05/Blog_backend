# Generated by Django 5.1 on 2024-10-27 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_suscriber_alter_blog_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Suscriber',
            new_name='Subscriber',
        ),
    ]
