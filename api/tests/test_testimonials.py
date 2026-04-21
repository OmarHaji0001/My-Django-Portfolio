from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from portfolio.models import Testimonial


class TestimonialAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Testimonial.objects.create(
            name='John Doe',
            role='Manager',
            feedback='Great work!',
            date_given='2024-01-01'
        )

    def test_testimonial_list_returns_200(self):
        response = self.client.get(reverse('testimonial-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_testimonial_returns_correct_fields(self):
        response = self.client.get(reverse('testimonial-list'))
        self.assertIn('name', response.data[0])
        self.assertIn('feedback', response.data[0])