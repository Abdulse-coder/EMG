from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from communication.models import Communication

User = get_user_model()

class CommunicationTests(APITestCase):

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
        self.communication_data = {
            "sender": "John Doe",
            "receiver": "Jane Doe",
            "subject": "Test Subject",
            "message": "This is a test message",
            "is_read": False
        }

    def test_create_communication(self):
        url = reverse('communication-list')
        response = self.client.post(url, self.communication_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Communication.objects.count(), 1)
        self.assertEqual(Communication.objects.get().sender, 'John Doe')

    def test_edit_communication(self):
        communication = Communication.objects.create(**self.communication_data)
        url = reverse('communication-detail', kwargs={'pk': communication.pk})
        updated_data = self.communication_data.copy()
        updated_data['subject'] = 'Updated Subject'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Communication.objects.get().subject, 'Updated Subject')

    def test_list_communications(self):
        Communication.objects.create(**self.communication_data)
        url = reverse('communication-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_view_communication(self):
        communication = Communication.objects.create(**self.communication_data)
        url = reverse('communication-detail', kwargs={'pk': communication.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sender'], 'John Doe')

    def test_delete_communication(self):
        communication = Communication.objects.create(**self.communication_data)
        url = reverse('communication-detail', kwargs={'pk': communication.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Communication.objects.count(), 0)
