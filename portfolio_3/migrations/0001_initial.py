# Generated by Django 4.2.7 on 2023-12-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='portfolio_3/image')),
                ('slide', models.ImageField(blank=True, upload_to='portfolio_3/slide')),
                ('low_title', models.CharField(blank=True, max_length=255)),
                ('low_about', models.CharField(blank=True, max_length=255)),
                ('blog_title', models.CharField(blank=True, max_length=255)),
                ('blog_photo', models.ImageField(blank=True, upload_to='portfolio_3/blogs_images')),
                ('time', models.DateField(blank=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('icons', models.ImageField(blank=True, upload_to='portfolio_3/icons/')),
            ],
            options={
                'verbose_name': 'Portfolio_3',
                'verbose_name_plural': 'Portfolio_3',
            },
        ),
    ]
