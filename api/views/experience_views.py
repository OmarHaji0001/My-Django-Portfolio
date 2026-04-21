from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from portfolio.models import Experience
from api.serializers import ExperienceSerializer


class NoPagination(PageNumberPagination):
    page_size = None


class ExperienceListView(generics.ListAPIView):
    """
    Returns a list of all experience entries ordered by start date.
    """
    queryset = Experience.objects.all().order_by('-start_date')
    serializer_class = ExperienceSerializer
    pagination_class = NoPagination