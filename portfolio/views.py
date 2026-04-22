from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .models import Banner, Project, PersonalInfo, Skill, Testimonial, BannerImages, ContactSubmission
from api.utils import send_contact_emails


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

        # Save to database always, regardless of email status
        ContactSubmission.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        try:
            send_contact_emails(name, email, subject, message)
        except Exception:
            pass

        # Always show success, msg is saved to DB regardless
        messages.success(request, "Your message has been received! I'll get back to you soon.")
        return redirect('contact')

    return render(request, 'pages/contact.html', {'banner': banner})


def download_cv(request):
    personal_info = PersonalInfo.objects.first()
    if personal_info and personal_info.pdfCV:
        return redirect(personal_info.pdfCV.url)
    raise Http404("CV file not found.")