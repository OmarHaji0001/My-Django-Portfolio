from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from drf_spectacular.utils import extend_schema
from api.serializers import ContactSubmissionSerializer
from api.utils import send_contact_emails


class ContactThrottle(AnonRateThrottle):
    rate = '5/hour'


class ContactView(APIView):
    """
    Handles contact form submissions.
    Saves to DB and sends an email via SendGrid.
    Throttled to 5 requests per hour.
    """
    throttle_classes = [ContactThrottle]

    @extend_schema(
        request=ContactSubmissionSerializer,
        responses={201: {'type': 'object', 'properties': {'success': {'type': 'string'}}}},
    )
    def post(self, request):
        serializer = ContactSubmissionSerializer(data=request.data)

        if serializer.is_valid():
            submission = serializer.save()

            try:
                send_contact_emails(
                    submission.name,
                    submission.email,
                    submission.subject,
                    submission.message
                )
            except Exception as e:
                return Response(
                    {'error': f'Email failed: {str(e)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response(
                {'success': 'Your message has been sent successfully!'},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)