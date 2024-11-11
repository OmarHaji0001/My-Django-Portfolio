from django.contrib import admin
from .models import *

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'job_title')
    search_fields = ('fname', 'lname', 'email', 'job_title')


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')
    search_fields = ('title',)
    list_filter = ('date_added',)
    inlines = [ProjectImageInline, TechnologyInline]


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    search_fields = ('name',)
    list_filter = ('project',)


admin.site.register(Skill)
admin.site.register(BannerImages)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company')
    list_filter = ('start_date', 'end_date')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'date_given')
    search_fields = ('name', 'role')
    list_filter = ('date_given',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('page', 'alt_text')
    search_fields = ('page',)
