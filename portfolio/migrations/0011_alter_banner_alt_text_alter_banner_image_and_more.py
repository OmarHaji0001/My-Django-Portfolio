# Generated by Django 5.1.2 on 2024-10-24 20:37

import ckeditor.fields
import cloudinary.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='alt_text',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='about',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='fname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='job_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='lname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='logo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='pdfCV',
            field=cloudinary.models.CloudinaryField(max_length=255, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='pdf'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
