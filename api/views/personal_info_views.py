from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from portfolio.models import PersonalInfo
from api.serializers import PersonalInfoSerializer


class PersonalInfoView(APIView):
    """
    Returns your personal info (single object, not a list).
    """
    def get(self, request):
        personal_info = PersonalInfo.objects.first()
        serializer = PersonalInfoSerializer(personal_info)
        return Response(serializer.data)