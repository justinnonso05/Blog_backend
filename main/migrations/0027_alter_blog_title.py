# Generated by Django 5.1 on 2024-11-07 22:18

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_subscriber_unsubscribe_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(help_text='No emojis allowed.', max_length=255, validators=[main.models.validate_no_emoji]),
        ),
    ]
