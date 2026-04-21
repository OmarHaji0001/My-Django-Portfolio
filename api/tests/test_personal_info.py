from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models import PersonalInfo


class PersonalInfoSingletonTest(TestCase):
    def test_cannot_create_second_personal_info(self):
        PersonalInfo.objects.create(
            fname='Omar',
            lname='Haji',
            phone='123456789',
            birthdate='2002-04-24',
            job_title='Developer',
            email='omar@test.com',
            country='Palestine',
            city='Nablus',
            street='Test Street',
            about='About me',
        )
        with self.assertRaises(ValidationError):
            PersonalInfo.objects.create(
                fname='Another',
                lname='Person',
                phone='987654321',
                birthdate='2000-01-01',
                job_title='Designer',
                email='another@test.com',
                country='Palestine',
                city='Nablus',
                street='Another Street',
                about='About another',
            )