from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from portfolio.models import Testimonial
from api.serializers import TestimonialSerializer


class NoPagination(PageNumberPagination):
    page_size = None


class TestimonialListView(generics.ListAPIView):
    """
    Returns a list of all testimonials.
    """
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    pagination_class = NoPagination