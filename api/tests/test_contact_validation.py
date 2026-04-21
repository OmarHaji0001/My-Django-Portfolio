from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from unittest.mock import patch


class ContactValidationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_data = {
            'name': 'Test User',
            'email': 'test@test.com',
            'subject': 'Test Subject',
            'message': 'Test message'
        }

    def post(self, data):
        with patch('api.views.contact_views.ContactThrottle.allow_request', return_value=True):
            return self.client.post(
                reverse('api-contact'),
                data,
                format='json'
            )

    def test_rejects_invalid_email_format(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'not-an-email'
        response = self.post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejects_email_without_domain(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'test@'
        response = self.post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejects_email_without_at_sign(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'testtest.com'
        response = self.post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejects_empty_name(self):
        invalid_data = self.valid_data.copy()
        invalid_data['name'] = ''
        response = self.post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejects_empty_message(self):
        invalid_data = self.valid_data.copy()
        invalid_data['message'] = ''
        response = self.post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejects_empty_subject(self):
        invalid_data = self.valid_data.copy()
        invalid_data['subject'] = ''
        response = self.post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejects_missing_email(self):
        invalid_data = self.valid_data.copy()
        del invalid_data['email']
        response = self.post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejects_missing_name(self):
        invalid_data = self.valid_data.copy()
        del invalid_data['name']
        response = self.post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejects_missing_message(self):
        invalid_data = self.valid_data.copy()
        del invalid_data['message']
        response = self.post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejects_missing_subject(self):
        invalid_data = self.valid_data.copy()
        del invalid_data['subject']
        response = self.post(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)