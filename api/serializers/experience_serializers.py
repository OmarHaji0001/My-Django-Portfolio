from rest_framework import serializers
from portfolio.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'id', 'title', 'company',
            'description', 'start_date', 'end_date'
        ]