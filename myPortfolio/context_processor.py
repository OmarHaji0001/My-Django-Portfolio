def personal_info(request):
    from portfolio.models import PersonalInfo
    personal_info = PersonalInfo.objects.first()
    return {
        'personal_info': personal_info,
        'spinner_image_url': personal_info.spinner_image.url if personal_info.spinner_image else None,
    }
