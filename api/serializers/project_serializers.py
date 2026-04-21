from rest_framework import serializers
from portfolio.models import Project, Technology, ProjectImage


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name']


class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = ['id', 'name', 'description', 'image']

    def get_image(self, obj):
        return obj.image.url if obj.image else None


class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'image',
            'link', 'github_link', 'created_date',
            'date_added', 'technologies', 'images'
        ]

    def get_image(self, obj):
        return obj.image.url if obj.image else None