# Generated by Django 4.2.7 on 2023-12-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features_1',
            name='blog_photo',
            field=models.ImageField(blank=True, upload_to='features_1/blogs_images'),
        ),
        migrations.AlterField(
            model_name='features_1',
            name='icons',
            field=models.ImageField(blank=True, upload_to='features_1/icons/'),
        ),
    ]
