from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from managment.models import WardAdmissionDischarge

User = get_user_model()

class WardAdmissionDischargeTests(APITestCase):

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
        self.ward_admission_discharge_data = {
            "patient_name": "John Doe",
            "admitted_by": "Dr. Smith",
            "ward_name": "Ward 1",
            "discharged_by": "Dr. Jane",
            "discharged_from_hospital": True,
            "discharge_remark": "Recovered",
            "discharge_date": "2023-01-01T00:00:00Z",
            "appointment": "Follow-up"
        }

    def test_create_ward_admission_discharge(self):
        url = reverse('wardadmissiondischarge-list')
        response = self.client.post(url, self.ward_admission_discharge_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WardAdmissionDischarge.objects.count(), 1)
        self.assertEqual(WardAdmissionDischarge.objects.get().patient_name, 'John Doe')

    def test_edit_ward_admission_discharge(self):
        ward_admission_discharge = WardAdmissionDischarge.objects.create(**self.ward_admission_discharge_data)
        url = reverse('wardadmissiondischarge-detail', kwargs={'pk': ward_admission_discharge.pk})
        updated_data = self.ward_admission_discharge_data.copy()
        updated_data['patient_name'] = 'Jane Doe'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(WardAdmissionDischarge.objects.get().patient_name, 'Jane Doe')

    def test_list_ward_admission_discharge(self):
        WardAdmissionDischarge.objects.create(**self.ward_admission_discharge_data)
        url = reverse('wardadmissiondischarge-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_view_ward_admission_discharge(self):
        ward_admission_discharge = WardAdmissionDischarge.objects.create(**self.ward_admission_discharge_data)
        url = reverse('wardadmissiondischarge-detail', kwargs={'pk': ward_admission_discharge.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['patient_name'], 'John Doe')

    def test_delete_ward_admission_discharge(self):
        ward_admission_discharge = WardAdmissionDischarge.objects.create(**self.ward_admission_discharge_data)
        url = reverse('wardadmissiondischarge-detail', kwargs={'pk': ward_admission_discharge.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(WardAdmissionDischarge.objects.count(), 0)

