# Generated by Django 5.1 on 2024-09-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=255),
        ),
    ]
