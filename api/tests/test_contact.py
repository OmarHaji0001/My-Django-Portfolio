from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from portfolio.models import ContactSubmission


class ContactAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_data = {
            'name': 'Test User',
            'email': 'test@test.com',
            'subject': 'Test Subject',
            'message': 'Test message'
        }

    def test_contact_saves_to_db(self):
        from unittest.mock import patch
        with patch('django.core.mail.EmailMessage.send'):
            self.client.post(
                reverse('contact'),
                self.valid_data,
                format='json'
            )
        self.assertEqual(ContactSubmission.objects.count(), 1)

    def test_contact_rejects_missing_fields(self):
        response = self.client.post(
            reverse('contact'),
            {'name': 'Test'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_contact_rejects_invalid_email(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'not-an-email'
        response = self.client.post(
            reverse('contact'),
            invalid_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)