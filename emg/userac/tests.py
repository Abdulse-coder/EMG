from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser

class UserTests(APITestCase):

    def setUp(self):
        self.user_data = {
            "user_name": "testuser",
            "password": "password123",
            "name": "Test",
            "father_name": "User",
            "grand_father_name": "Test",
            "date_of_birth": "1990-01-01",
            "region": "Region",
            "city": "City",
            "religion": "Religion",
            "phone_number": "1234567890",
            "emergency_name": "Emergency",
            "emergency_phone": "0987654321",
            "created_by": "admin",
            "status": "A",
            "type_of_account": "standard"
        }
        self.user = CustomUser.objects.create_user(
            user_name="admin",
            password="adminpass",
            name="Admin",
            father_name="User",
            grand_father_name="Admin",
            date_of_birth="1980-01-01",
            region="Region",
            city="City",
            religion="Religion",
            phone_number="1234567890",
            emergency_name="Emergency",
            emergency_phone="0987654321",
            created_by="system",
            status="A",
            type_of_account="admin",
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        self.client.login(username='admin', password='adminpass')

    def test_create_user(self):
        response = self.client.post(reverse('user-list'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_user_detail(self):
        user = CustomUser.objects.create_user(**self.user_data)
        response = self.client.get(reverse('user-detail', kwargs={'pk': user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user_name'], user.user_name)

    def test_update_user(self):
        user = CustomUser.objects.create_user(**self.user_data)
        updated_data = self.user_data.copy()
        updated_data['name'] = 'Updated Name'
        response = self.client.put(reverse('user-detail', kwargs={'pk': user.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Name')

    def test_delete_user(self):
        user = CustomUser.objects.create_user(**self.user_data)
        response = self.client.delete(reverse('user-detail', kwargs={'pk': user.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(CustomUser.objects.filter(pk=user.pk).exists())

