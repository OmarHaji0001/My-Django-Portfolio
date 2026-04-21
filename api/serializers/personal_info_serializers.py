from rest_framework import serializers
from portfolio.models import PersonalInfo


class PersonalInfoSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = PersonalInfo
        fields = [
            'id', 'fname', 'lname', 'phone', 'photo',
            'birthdate', 'job_title', 'email', 'country',
            'city', 'about', 'facebook', 'instagram',
            'linkedin', 'github', 'availability'
        ]

    def get_photo(self, obj):
        return obj.photo.url if obj.photo else None