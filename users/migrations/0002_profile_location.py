# Generated by Django 3.1.2 on 2020-11-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Location',
            field=models.CharField(blank=True, default='Nairobi', max_length=250),
        ),
    ]