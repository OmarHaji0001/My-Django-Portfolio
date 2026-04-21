from rest_framework import serializers
from portfolio.models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'role', 'feedback', 'image', 'date_given']

    def get_image(self, obj):
        return obj.image.url if obj.image else None