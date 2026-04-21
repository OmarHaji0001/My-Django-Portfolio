from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from portfolio.models import Experience


class ExperienceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Experience.objects.create(
            title='Developer',
            company='Test Company',
            description='Test description',
            start_date='2024-01-01',
            end_date='2024-06-01'
        )

    def test_experience_list_returns_200(self):
        response = self.client.get(reverse('experience-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_experience_returns_correct_fields(self):
        response = self.client.get(reverse('experience-list'))
        self.assertIn('title', response.data[0])
        self.assertIn('company', response.data[0])
        self.assertIn('start_date', response.data[0])