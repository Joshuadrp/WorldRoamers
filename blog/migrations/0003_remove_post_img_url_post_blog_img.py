# Generated by Django 5.1 on 2024-09-17 12:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_remove_post_location_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_url',
        ),
        migrations.AddField(
            model_name='post',
            name='blog_img',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
