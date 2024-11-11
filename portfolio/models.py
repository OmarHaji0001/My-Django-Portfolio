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
    photo = CloudinaryField('photo')
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
    skills_background_image = CloudinaryField('skills_background_image', blank=True, null=True)
    spinner_image = CloudinaryField('spinner_image', blank=True, null=True)
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
    image = CloudinaryField('project_image', blank=True, null=True)
    pdfCV = CloudinaryField('pdf_documentation', blank=True, null=True)
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
    image = CloudinaryField('ProjectImage')
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
    image = CloudinaryField('Testimonial_Image', blank=True, null=True)
    date_given = models.DateField()

    def __str__(self):
        return f"Testimonial from {self.name}"


class Banner(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('skills', 'Skills'),
        ('contact', 'Contact'),
    ]

    page = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True)
    image = CloudinaryField('Banner_Image')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return f"Banner for {self.get_page_display()}"


class BannerImages(models.Model):
    background = CloudinaryField('background', blank=True, null=True)
    fog_7 = CloudinaryField('fog_7', blank=True, null=True)
    mountain_10 = CloudinaryField('mountain_10', blank=True, null=True)
    mountain_9 = CloudinaryField('mountain_9', blank=True, null=True)
    mountain_8 = CloudinaryField('mountain_8', blank=True, null=True)
    fog_5 = CloudinaryField('fog_5', blank=True, null=True)
    mountain_7 = CloudinaryField('mountain_7', blank=True, null=True)
    mountain_6 = CloudinaryField('mountain_6', blank=True, null=True)
    fog_4 = CloudinaryField('fog_4', blank=True, null=True)
    mountain_5 = CloudinaryField('mountain_5', blank=True, null=True)
    fog_3 = CloudinaryField('fog_3', blank=True, null=True)
    mountain_4 = CloudinaryField('mountain_4', blank=True, null=True)
    mountain_3 = CloudinaryField('mountain_3', blank=True, null=True)
    fog_2 = CloudinaryField('fog_2', blank=True, null=True)
    mountain_2 = CloudinaryField('mountain_2', blank=True, null=True)
    mountain_1 = CloudinaryField('mountain_1', blank=True, null=True)
    sun_rays = CloudinaryField('sun_rays', blank=True, null=True)
    black_shadow = CloudinaryField('black_shadow', blank=True, null=True)
    fog_1 = CloudinaryField('fog_1', blank=True, null=True)

    def __str__(self):
        return "3D Banner Images"
