from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Banner, Project, PersonalInfo, Skill, Testimonial, BannerImages
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings  # Add this import
from django.views.decorators.csrf import csrf_protect


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


@csrf_protect
def contact(request):
    banner = get_object_or_404(Banner, page='contact')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Professional email content that avoids spam filters
        email_subject = f"Portfolio Contact Form: {subject}"
        email_body = f"""Hello Omar,

You have received a new contact form submission from your portfolio website.

Contact Details:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name: {name}
Email: {email}
Subject: {subject}

Message:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This message was sent from: https://omar-haji-portfolio.vercel.app/contact/

To reply to {name}, simply respond to this email.

Best regards,
Omar Haji Portfolio System
        """

        try:
            # SendGrid EmailMessage with better headers
            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
                headers={
                    'From': f"Omar Haji Portfolio <{settings.DEFAULT_FROM_EMAIL}>",
                    'X-Mailer': 'Django Portfolio Contact Form',
                    'X-Priority': '3',
                }
            )

            email_message.send(fail_silently=False)
            messages.success(request, "Your message has been sent successfully!")

        except Exception as e:
            messages.error(request, "Sorry, there was an error sending your message. Please try again later.")
            print(f"Email error: {e}")

        return redirect('contact')

    return render(request, 'pages/contact.html', {'banner': banner})


def download_cv(request):
    personal_info = PersonalInfo.objects.first()

    if personal_info.pdfCV:
        cv_url = personal_info.pdfCV.url
        return redirect(cv_url)
    else:
        raise Http404("CV file not found.")
