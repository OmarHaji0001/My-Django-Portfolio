from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from django.core.mail import EmailMessage
from django.conf import settings
from drf_spectacular.utils import extend_schema
from api.serializers import ContactSubmissionSerializer


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

            # Email to you
            email_subject = f"{submission.subject} - From {submission.name}"
            email_body = f"""
From: {submission.name} <{submission.email}>
Subject: {submission.subject}

{submission.message}

---
Reply to this email to respond directly to {submission.name} at {submission.email}
            """

            # Auto-reply to sender
            auto_reply_subject = "Thanks for reaching out — Omar Haji"
            auto_reply_body = f"""
Hi {submission.name},

Thank you for your message! I've received it and will get back to you as soon as possible.

Here's a copy of your message:
---
Subject: {submission.subject}

{submission.message}
---

Best regards,
Omar Haji
contact@omarhaji.com
www.omarhaji.com
            """

            try:
                # Send email to you
                email_message = EmailMessage(
                    subject=email_subject,
                    body=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.CONTACT_EMAIL],
                    reply_to=[submission.email],
                )
                email_message.send(fail_silently=False)

                # Send auto-reply to sender
                auto_reply = EmailMessage(
                    subject=auto_reply_subject,
                    body=auto_reply_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[submission.email],
                    bcc=[settings.CONTACT_EMAIL],
                )
                auto_reply.send(fail_silently=False)

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