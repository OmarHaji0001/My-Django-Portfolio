from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from portfolio.models import Project, Technology


class ProjectAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project = Project.objects.create(
            title='Test Project',
            description='Test Description',
        )
        Technology.objects.create(
            project=self.project,
            name='Django'
        )

    def test_project_list_returns_200(self):
        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_list_returns_correct_fields(self):
        response = self.client.get(reverse('project-list'))
        results = response.data['results']
        self.assertIn('id', results[0])
        self.assertIn('title', results[0])
        self.assertIn('technologies', results[0])
        self.assertIn('images', results[0])

    def test_project_detail_returns_200(self):
        response = self.client.get(
            reverse('project-detail', kwargs={'pk': self.project.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_detail_returns_correct_title(self):
        response = self.client.get(
            reverse('project-detail', kwargs={'pk': self.project.pk})
        )
        self.assertEqual(response.data['title'], 'Test Project')

    def test_project_detail_404_for_invalid_id(self):
        response = self.client.get(
            reverse('project-detail', kwargs={'pk': 9999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)