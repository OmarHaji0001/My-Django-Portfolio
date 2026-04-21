from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.decorators.csrf import csrf_protect

from .models import Banner, Project, PersonalInfo, Skill, Testimonial, BannerImages


def custom_404_view(request, exception):
    if request.path.startswith('/api/'):
        return JsonResponse({'error': 'Not found'}, status=404)
    return redirect('home')


def home(request):
    banner = get_object_or_404(Banner, page='home')
    projects = Project.objects.prefetch_related('technologies')
    testimonials = Testimonial.objects.all()
    context = {
        'projects': projects,
        'banner': banner,
        'testimonials': testimonials,
    }
    return render(request, 'pages/home.html', context)


def projects(request):
    all_projects = Project.objects.all()
    banner_images = BannerImages.objects.first()
    context = {
        'projects': all_projects,
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
    all_skills = Skill.objects.all()
    context = {
        'banner': banner,
        'background_image': personal_info.skills_background_image.url if personal_info.skills_background_image else None,
        'skills': all_skills,
    }
    return render(request, 'pages/skills.html', context)


@csrf_protect
def contact(request):
    banner = get_object_or_404(Banner, page='contact')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email_subject = f"{subject} - From {name}"
        email_body = f"""
From: {name} <{email}>
Subject: {subject}

{message}

---
Reply to this email to respond directly to {name} at {email}
        """

        auto_reply_subject = "Thanks for reaching out — Omar Haji"
        auto_reply_body = f"""
Hi {name},

Thank you for your message! I've received it and will get back to you as soon as possible.

Here's a copy of your message:
---
Subject: {subject}

{message}
---

Best regards,
Omar Haji
contact@omarhaji.com
www.omarhaji.com
        """

        try:
            # Send email to Omar
            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )
            email_message.send(fail_silently=False)

            # Send auto-reply to sender
            auto_reply = EmailMessage(
                subject=auto_reply_subject,
                body=auto_reply_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
            auto_reply.send(fail_silently=False)

            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending message: {str(e)}")

        return redirect('contact')

    return render(request, 'pages/contact.html', {'banner': banner})


def download_cv(request):
    personal_info = PersonalInfo.objects.first()
    if personal_info and personal_info.pdfCV:
        return redirect(personal_info.pdfCV.url)
    raise Http404("CV file not found.")