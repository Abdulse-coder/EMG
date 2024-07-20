from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from ai.models import Access, Recommadtion  # Replace 'myapp' with your app name

User = get_user_model()

class APITestBase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            user_name="testuser",
            password="testpass123",
            name="Test",
            father_name="User",
            grand_father_name="TestUser",
            date_of_birth="1990-01-01",
            region="Region",
            city="City",
            religion="Religion",
            phone_number="1234567890",
            emergency_name="Emergency",
            emergency_phone="0987654321",
            created_by="Admin",
            status="A",
            type_of_account="Admin"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

class AccessTests(APITestBase):

    def setUp(self):
        super().setUp()
        self.access_data = {
            "accessed_card": "Card123",
            "accessed_by": "User123",
            "is_abnormal": False
        }

    def test_create_access(self):
        url = reverse('access-list')
        response = self.client.post(url, self.access_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Access.objects.count(), 1)
        self.assertEqual(Access.objects.get().accessed_card, 'Card123')

    def test_edit_access(self):
        access = Access.objects.create(**self.access_data)
        url = reverse('access-detail', kwargs={'pk': access.pk})
        updated_data = self.access_data.copy()
        updated_data['accessed_card'] = 'Card456'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Access.objects.get().accessed_card, 'Card456')

    def test_list_accesses(self):
        Access.objects.create(**self.access_data)
        url = reverse('access-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_view_access(self):
        access = Access.objects.create(**self.access_data)
        url = reverse('access-detail', kwargs={'pk': access.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['accessed_card'], 'Card123')

    def test_delete_access(self):
        access = Access.objects.create(**self.access_data)
        url = reverse('access-detail', kwargs={'pk': access.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Access.objects.count(), 0)

class RecommadtionTests(APITestBase):

    def setUp(self):
        super().setUp()
        self.recommadtion_data = {
            "client_name": "Client123",
            "title": "Title123",
            "recommadtion": "Recommadtion text",
            "education": "Education text"
        }

    def test_create_recommadtion(self):
        url = reverse('recommadtion-list')
        response = self.client.post(url, self.recommadtion_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recommadtion.objects.count(), 1)
        self.assertEqual(Recommadtion.objects.get().client_name, 'Client123')

    def test_edit_recommadtion(self):
        recommadtion = Recommadtion.objects.create(**self.recommadtion_data)
        url = reverse('recommadtion-detail', kwargs={'pk': recommadtion.pk})
        updated_data = self.recommadtion_data.copy()
        updated_data['title'] = 'Updated Title'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Recommadtion.objects.get().title, 'Updated Title')

    def test_list_recommadtions(self):
        Recommadtion.objects.create(**self.recommadtion_data)
        url = reverse('recommadtion-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_view_recommadtion(self):
        recommadtion = Recommadtion.objects.create(**self.recommadtion_data)
        url = reverse('recommadtion-detail', kwargs={'pk': recommadtion.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['client_name'], 'Client123')

    def test_delete_recommadtion(self):
        recommadtion = Recommadtion.objects.create(**self.recommadtion_data)
        url = reverse('recommadtion-detail', kwargs={'pk': recommadtion.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Recommadtion.objects.count(), 0)
