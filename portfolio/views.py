from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Banner, Project, PersonalInfo, Skill, ContactSubmission, Testimonial
from django.contrib import messages


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
    banner = get_object_or_404(Banner, page='projects')
    context = {
        'projects': projects,
        'banner': banner,
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

        ContactSubmission.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been submitted successfully!")

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
