# Generated by Django 4.2.7 on 2023-11-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='home_1/image')),
                ('slide', models.ImageField(blank=True, upload_to='home_1/slide')),
                ('low_title', models.CharField(blank=True, max_length=255)),
                ('low_about', models.CharField(blank=True, max_length=255)),
                ('blog_title', models.CharField(blank=True, max_length=255)),
                ('blog_photo', models.ImageField(blank=True, upload_to='home_1/blogs_images')),
                ('time', models.DateField(blank=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('icons', models.ImageField(blank=True, upload_to='home_1/icons/')),
            ],
            options={
                'verbose_name': 'Home_1',
                'verbose_name_plural': 'Homes_1',
            },
        ),
    ]
