from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from portfolio.models import Skill
from api.serializers import SkillSerializer


class NoPagination(PageNumberPagination):
    page_size = None


class SkillListView(generics.ListAPIView):
    """
    Returns a list of all skills.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    pagination_class = NoPagination