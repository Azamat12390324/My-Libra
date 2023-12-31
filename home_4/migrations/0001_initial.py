# Generated by Django 4.2.7 on 2023-11-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
                ('about', models.TextField(blank=True)),
                ('icons', models.ImageField(blank=True, upload_to='home_4/=icons')),
                ('image', models.ImageField(blank=True, upload_to='home_4/images')),
                ('image_name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Home_4',
                'verbose_name_plural': 'Homes_4',
            },
        ),
    ]
