# Generated by Django 4.0.2 on 2022-11-20 14:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_bet_played'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
