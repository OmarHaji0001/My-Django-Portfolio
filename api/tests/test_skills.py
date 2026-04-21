from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from portfolio.models import Skill


class SkillAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Skill.objects.create(name='Python')
        Skill.objects.create(name='Django')

    def test_skill_list_returns_200(self):
        response = self.client.get(reverse('skill-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_skill_list_returns_all_skills(self):
        response = self.client.get(reverse('skill-list'))
        self.assertEqual(len(response.data), 2)