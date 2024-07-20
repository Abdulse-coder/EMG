from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import PharmacyOrder
from userac.models import CustomUser  # Import your custom user model

class PharmacyOrderTests(APITestCase):
    def setUp(self):
        # Create a user using the custom user model
        self.user = CustomUser.objects.create_user(
            user_name='testuser', 
            password='testpass',
            name='Test', 
            father_name='User', 
            grand_father_name='Test',
            date_of_birth='1990-01-01',
            region='Region',
            city='City',
            religion='Religion',
            phone_number='1234567890',
            emergency_name='Emergency Contact',
            emergency_phone='0987654321',
            created_by='admin',
            status='A',
            type_of_account='Type',
            is_active=True,
            is_staff=True,  # Set to True if necessary for admin access
        )
        self.client.login(username='testuser', password='testpass')

    def test_create_pharmacy_order(self):
        url = reverse('pharmacyorder-list')
        data = {
            'order_number': '12345',
            'patient_name': 'John Doe',
            'health_provider_name': 'Dr. Smith',
            'pharmacist_name': 'Jane Doe',
            'drug_name': 'Paracetamol',
            'quantity': 10,
            'full_order_details': 'Take one tablet daily',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_pharmacy_orders(self):
        PharmacyOrder.objects.create(
            order_number='12345',
            patient_name='John Doe',
            health_provider_name='Dr. Smith',
            pharmacist_name='Jane Doe',
            drug_name='Paracetamol',
            quantity=10,
            full_order_details='Take one tablet daily',
        )
        url = reverse('pharmacyorder-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_pharmacy_order(self):
        order = PharmacyOrder.objects.create(
            order_number='12345',
            patient_name='John Doe',
            health_provider_name='Dr. Smith',
            pharmacist_name='Jane Doe',
            drug_name='Paracetamol',
            quantity=10,
            full_order_details='Take one tablet daily',
        )
        url = reverse('pharmacyorder-detail', kwargs={'pk': order.pk})
        data = {
            'order_number': '12345',
            'patient_name': 'John Doe',
            'health_provider_name': 'Dr. Smith',
            'pharmacist_name': 'Jane Doe',
            'drug_name': 'Ibuprofen',
            'quantity': 20,
            'full_order_details': 'Take two tablets daily',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_pharmacy_order(self):
        order = PharmacyOrder.objects.create(
            order_number='12345',
            patient_name='John Doe',
            health_provider_name='Dr. Smith',
            pharmacist_name='Jane Doe',
            drug_name='Paracetamol',
            quantity=10,
            full_order_details='Take one tablet daily',
        )
        url = reverse('pharmacyorder-detail', kwargs={'pk': order.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)