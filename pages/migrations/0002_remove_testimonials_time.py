# Generated by Django 4.2.7 on 2023-12-10 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonials',
            name='time',
        ),
    ]