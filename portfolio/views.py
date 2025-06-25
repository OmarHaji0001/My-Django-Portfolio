from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Banner, Project, PersonalInfo, Skill, ContactSubmission, Testimonial, BannerImages
from django.contrib import messages
from django.core.mail import send_mail  # Add this import
from django.conf import settings  # Add this import


def custom_404_view(request, exception):
    return redirect('home')


def home(request):
    banner = get_object_or_404(Banner, page='home')
    projects = Project.objects.prefetch_related('technologies').order_by('created_date')
    testimonials = Testimonial.objects.all()

    context = {
        'projects': projects,
        'banner': banner,
        'testimonials': testimonials,
    }
    return render(request, 'pages/home.html', context)


def projects(request):
    projects = Project.objects.all().order_by('created_date')
    banner_images = BannerImages.objects.first()
    context = {
        'projects': projects,
        'banner_images': banner_images,
    }
    return render(request, 'pages/projects.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    images = project.images.all()
    return render(request, 'pages/project_detail.html', {'project': project, 'images': images})


def skills(request):
    banner = get_object_or_404(Banner, page='skills')
    personal_info = get_object_or_404(PersonalInfo)
    skills = Skill.objects.all()
    context = {
        'banner': banner,
        'background_image': personal_info.skills_background_image.url if personal_info.skills_background_image else None,
        'skills': skills,
    }
    return render(request, 'pages/skills.html', context)


def contact(request):
    banner = get_object_or_404(Banner, page='contact')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create email content - this is the key part
        email_subject = f"{subject} - From {name}"
        email_body = f"""
From: {name} <{email}>
Subject: {subject}

{message}

---
Reply to this email to respond directly to {name} at {email}
        """

        try:
            # Send email using SendGrid
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,  # This will be your verified email
                recipient_list=[settings.CONTACT_EMAIL],  # Your email
                reply_to=[email],  # This is the magic - when you hit reply, it goes to their email!
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")

        except Exception as e:
            messages.error(request, "Sorry, there was an error sending your message. Please try again later.")
            print(f"Email sending error: {e}")

        return redirect('contact')

    return render(request, 'pages/contact.html', {'banner': banner})



# def contact(request):
#     banner = get_object_or_404(Banner, page='contact')
#
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#
#         ContactSubmission.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message
#         )
#
#         messages.success(request, "Your message has been submitted successfully!")
#
#         return redirect('contact')
#
#     return render(request, 'pages/contact.html', {'banner': banner})


# def contact(request):
#     banner = get_object_or_404(Banner, page='contact')
#
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_HOST_USER,
#             [email],
#             fail_silently=False,
#         )
#     return render(request, 'pages/contact.html', {'banner': banner})


def download_cv(request):
    personal_info = PersonalInfo.objects.first()

    if personal_info.pdfCV:
        cv_url = personal_info.pdfCV.url
        return redirect(cv_url)
    else:
        raise Http404("CV file not found.")
