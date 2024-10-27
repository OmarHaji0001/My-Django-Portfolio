from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"


class PersonalInfo(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    photo = CloudinaryField('image')
    birthdate = models.DateField()
    job_title = models.CharField(max_length=50)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    about = RichTextField()
    pdfCV = CloudinaryField('pdf')
    skills_background_image = CloudinaryField('image', blank=True, null=True)
    spinner_image = CloudinaryField('image', blank=True, null=True)
    availability = models.CharField(
        max_length=20,
        choices=[('available', 'Available'), ('not_available', 'Not Available')],
        default='available'
    )

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    pdfCV = CloudinaryField('pdf', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    created_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Technology(models.Model):
    project = models.ForeignKey(Project, related_name='technologies', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"Image for {self.project.title}: {self.name}"


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company if self.company else 'N/A'}"


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True, null=True)
    feedback = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    date_given = models.DateField()

    def __str__(self):
        return f"Testimonial from {self.name}"


class Banner(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('projects', 'Projects'),
        ('skills', 'Skills'),
        ('contact', 'Contact'),
    ]

    page = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True)
    image = CloudinaryField('image')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return f"Banner for {self.get_page_display()}"
