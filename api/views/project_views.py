from rest_framework import generics
from portfolio.models import Project
from api.serializers import ProjectSerializer


class ProjectListView(generics.ListAPIView):
    """
    Returns a list of all projects ordered by created date.
    """
    queryset = Project.objects.prefetch_related(
        'technologies', 'images'
    ).order_by('created_date')
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    """
    Returns a single project by ID.
    """
    queryset = Project.objects.prefetch_related(
        'technologies', 'images'
    )
    serializer_class = ProjectSerializer