from django.urls import reverse
from rest_framework.test import APITestCase

from app_users.models import CustomUser
from app_organizations.models import Organizations


class OrganizationsTests(APITestCase):

    """
    тестирование serializer Organizations
    """

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='testuser@test.com',
            password='testpassword',
            first_name='First_name',
            last_name='Last_name',
        )
        self.organization = Organizations.objects.create(
            name='TestOrganization', description='descriptiontest')

    def test_list_organizations(self):
        url = reverse('organizations')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_organization(self):

        url = reverse('organizations_create')
        self.client.force_authenticate(user=self.user)
        data = {'name': 'NEWOrganization', 'description': 'NEWdescription'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data['name'], 'NEWOrganization')
        self.assertEqual(response.status_code, 201)
