from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from app_users.models import CustomUser
from app_users.serializers import UserSerializer, LoginSerializer, UserRegisterSerializer
from app_organizations.models import Organizations


class UserAPITest(APITestCase):

    """
    Тестирование serializers Users
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='testuser@test.com',
            password='testpassword',
            first_name='First_name',
            last_name='Last_name',
        )

    def test_list_users(self):
        url = reverse('users_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_user(self):
        url = reverse('user_detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], UserRegisterSerializer(self.user).data['email'])

    def test_update_user_profile(self):
        self.client.force_authenticate(user=self.user)
        uel = reverse('user_profile')
        data = {'first_name': 'New_first_name', 'last_name': 'New_last_name'}
        response = self.client.put(uel, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['first_name'], 'New_first_name')
        self.assertEqual(response.data['last_name'], 'New_last_name')

    def test_user_registration(self):
        url = reverse('user_registration')
        data = {'email': 'newtestuser@test.com', 'password': 'testpassword',
                'password2': 'testpassword', 'first_name': 'NewUser', 'last_name': 'NewUserTest'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CustomUser.objects.count(), 2)
        user = CustomUser.objects.last()
        self.assertEqual(user.first_name, 'NewUser')

    def test_user_login(self):
        url = reverse('user_login')
        data = {'email': 'testuser@test.com', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        url = reverse('user_logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(user=self.user)
        response_authenticate = self.client.get(url)
        self.assertEqual(response_authenticate.status_code, 200)


class OrganizationsAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.organization = Organizations.objects.create(name='Test Organization')

    def test_list_organizations_users(self):
        url = reverse('organizations_users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
