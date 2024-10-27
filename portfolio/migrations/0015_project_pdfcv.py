# Generated by Django 5.1.2 on 2024-10-24 23:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_alter_personalinfo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pdfCV',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='pdf'),
        ),
    ]