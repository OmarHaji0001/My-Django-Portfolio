from django.urls import path
from api.views import (
    ProjectListView,
    ProjectDetailView,
    PersonalInfoView,
    SkillListView,
    ExperienceListView,
    TestimonialListView,
    ContactView,
)

urlpatterns = [
    # Projects
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    # Personal Info
    path('personal-info/', PersonalInfoView.as_view(), name='personal-info'),

    # Skills
    path('skills/', SkillListView.as_view(), name='skill-list'),

    # Experience
    path('experience/', ExperienceListView.as_view(), name='experience-list'),

    # Testimonials
    path('testimonials/', TestimonialListView.as_view(), name='testimonial-list'),

    # Contact
    path('contact/', ContactView.as_view(), name='contact'),
]