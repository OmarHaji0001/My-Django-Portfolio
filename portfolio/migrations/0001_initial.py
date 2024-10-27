# Generated by Django 5.1.2 on 2024-10-19 12:57

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='First Name')),
                ('lname', models.CharField(max_length=50, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('photo', models.ImageField(upload_to='images/%Y/%m/%d/%H/%M/%S/', verbose_name='Profile Picture')),
                ('birthdate', models.DateField(verbose_name='Birth Date')),
                ('job_title', models.CharField(max_length=50, verbose_name='Job Title')),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True, verbose_name='Personal Website')),
                ('about', ckeditor.fields.RichTextField(verbose_name='About Me')),
                ('pdfCV', models.FileField(upload_to='pdf/%Y/%m/%d/%H/%M/%S/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='PDF CV')),
                ('logo', models.ImageField(upload_to='images/logo/%Y/%m/%d/%H/%M/%S/', verbose_name='Logo')),
                ('twitter', models.URLField(blank=True, null=True)),
                ('availability', models.CharField(choices=[('available', 'Available'), ('not_available', 'Not Available')], default='available', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('tech_stack', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='projects/')),
                ('link', models.URLField(blank=True, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('proficiency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(blank=True, max_length=200, null=True)),
                ('feedback', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials/')),
                ('date_given', models.DateField()),
            ],
        ),
    ]
