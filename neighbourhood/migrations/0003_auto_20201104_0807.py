# Generated by Django 3.1.2 on 2020-11-04 08:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0002_auto_20201102_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default.jpg', max_length=255, verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default.jpg', max_length=255, verbose_name='images'),
        ),
    ]