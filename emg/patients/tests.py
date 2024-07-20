# File: tests/test_views.py

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from userac.models import CustomUser  # Import the CustomUser model
from patients.models import History, FreeHistory, Chart, Medication, Order, Consent, Intervention

class APITestBase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            user_name='testuser',
            password='testpassword',
            name='Test Name',
            father_name='Test Father',
            grand_father_name='Test Grandfather',
            date_of_birth='2000-01-01',
            region='Test Region',
            city='Test City',
            religion='Test Religion',
            phone_number='1234567890',
            emergency_name='Emergency Contact',
            emergency_phone='0987654321',
            created_by='Admin',
            status='A',
            type_of_account='Test Account'
        )
        self.client.force_authenticate(user=self.user)

class HistoryTests(APITestBase):
    def test_create_history(self):
        url = reverse('history-list')
        data = {
            "client_name": "Test Client",
            "health_pro_name": "Test Pro",
            "chief_complaint": "Test Complaint",
            "gravida": "G1",
            "para": "P0",
            "abortion": "A0",
            "stillbirth": "S0",
            "early_neonatal_death": "E0",
            "present_history": "No issues",
            "past_obs_history": "No past obs history",
            "menstrual_history": "Regular",
            "sexual_history": "N/A",
            "family_planning": "None",
            "gynecological_history": "No issues",
            "medical_history": "Healthy",
            "family_history": "Healthy family",
            "medication_history": "No medications",
            "surgical_history": "No surgeries",
            "nutritional_history": "Balanced diet",
            "diagnosis": "Healthy",
            "general_appearance": "Good",
            "skin": "Normal",
            "head": "Normal",
            "eye": "Normal",
            "ear": "Normal",
            "nose": "Normal",
            "throat": "Normal",
            "cardiovascular": "Normal",
            "respiratory": "Normal",
            "gastrointestinal": "Normal",
            "genitourinary": "Normal",
            "musculoskeletal": "Normal",
            "neurological": "Normal",
            "psychiatric": "Normal",
            "endocrine": "Normal",
            "immune": "Normal",
            "breast": "Normal",
            "blood_pressure": "120/80",
            "respiratory_rate": "16",
            "temperature": "36.5",
            "pulse_rate": "72",
            "spo2": "98%",
            "weight": "70kg"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_histories(self):
        url = reverse('history-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_history(self):
        history = History.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", chief_complaint="Test Complaint",
            gravida="G1", para="P0", abortion="A0", stillbirth="S0", early_neonatal_death="E0",
            present_history="No issues", past_obs_history="No past obs history", menstrual_history="Regular",
            sexual_history="N/A", family_planning="None", gynecological_history="No issues", medical_history="Healthy",
            family_history="Healthy family", medication_history="No medications", surgical_history="No surgeries",
            nutritional_history="Balanced diet", diagnosis="Healthy", general_appearance="Good", skin="Normal",
            head="Normal", eye="Normal", ear="Normal", nose="Normal", throat="Normal", cardiovascular="Normal",
            respiratory="Normal", gastrointestinal="Normal", genitourinary="Normal", musculoskeletal="Normal",
            neurological="Normal", psychiatric="Normal", endocrine="Normal", immune="Normal", breast="Normal",
            blood_pressure="120/80", respiratory_rate="16", temperature="36.5", pulse_rate="72", spo2="98%", weight="70kg"
        )
        url = reverse('history-detail', args=[history.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_history(self):
        history = History.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", chief_complaint="Test Complaint",
            gravida="G1", para="P0", abortion="A0", stillbirth="S0", early_neonatal_death="E0",
            present_history="No issues", past_obs_history="No past obs history", menstrual_history="Regular",
            sexual_history="N/A", family_planning="None", gynecological_history="No issues", medical_history="Healthy",
            family_history="Healthy family", medication_history="No medications", surgical_history="No surgeries",
            nutritional_history="Balanced diet", diagnosis="Healthy", general_appearance="Good", skin="Normal",
            head="Normal", eye="Normal", ear="Normal", nose="Normal", throat="Normal", cardiovascular="Normal",
            respiratory="Normal", gastrointestinal="Normal", genitourinary="Normal", musculoskeletal="Normal",
            neurological="Normal", psychiatric="Normal", endocrine="Normal", immune="Normal", breast="Normal",
            blood_pressure="120/80", respiratory_rate="16", temperature="36.5", pulse_rate="72", spo2="98%", weight="70kg"
        )
        url = reverse('history-detail', args=[history.id])
        data = {"chief_complaint": "Updated Complaint"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        history.refresh_from_db()
        self.assertEqual(history.chief_complaint, "Updated Complaint")

    def test_delete_history(self):
        history = History.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", chief_complaint="Test Complaint",
            gravida="G1", para="P0", abortion="A0", stillbirth="S0", early_neonatal_death="E0",
            present_history="No issues", past_obs_history="No past obs history", menstrual_history="Regular",
            sexual_history="N/A", family_planning="None", gynecological_history="No issues", medical_history="Healthy",
            family_history="Healthy family", medication_history="No medications", surgical_history="No surgeries",
            nutritional_history="Balanced diet", diagnosis="Healthy", general_appearance="Good", skin="Normal",
            head="Normal", eye="Normal", ear="Normal", nose="Normal", throat="Normal", cardiovascular="Normal",
            respiratory="Normal", gastrointestinal="Normal", genitourinary="Normal", musculoskeletal="Normal",
            neurological="Normal", psychiatric="Normal", endocrine="Normal", immune="Normal", breast="Normal",
            blood_pressure="120/80", respiratory_rate="16", temperature="36.5", pulse_rate="72", spo2="98%", weight="70kg"
        )
        url = reverse('history-detail', args=[history.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class FreeHistoryTests(APITestBase):
    def test_create_free_history(self):
        url = reverse('freehistory-list')
        data = {
            "client_name": "Test Client",
            "history": "Test History",
            "health_pro_name": "Test Pro"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_free_histories(self):
        url = reverse('freehistory-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_free_history(self):
        free_history = FreeHistory.objects.create(
            client_name="Test Client", history="Test History", health_pro_name="Test Pro"
        )
        url = reverse('freehistory-detail', args=[free_history.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_free_history(self):
        free_history = FreeHistory.objects.create(
            client_name="Test Client", history="Test History", health_pro_name="Test Pro"
        )
        url = reverse('freehistory-detail', args=[free_history.id])
        data = {"history": "Updated History"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        free_history.refresh_from_db()
        self.assertEqual(free_history.history, "Updated History")

    def test_delete_free_history(self):
        free_history = FreeHistory.objects.create(
            client_name="Test Client", history="Test History", health_pro_name="Test Pro"
        )
        url = reverse('freehistory-detail', args=[free_history.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ChartTests(APITestBase):
    def test_create_chart(self):
        url = reverse('chart-list')
        data = {
            "client_name": "Test Client",
            "health_pro_name": "Test Pro",
            "purpose": "Test Purpose",
            "blood_pressure": "120/80",
            "respiratory_rate": "16",
            "temperature": "36.5",
            "pulse_rate": "72",
            "spo2": "98%",
            "fetal_heart_rate": "150",
            "abdominal_pain": "None",
            "vaginal_bleeding": "None",
            "rash": "None",
            "itching": "None",
            "vomiting": "None",
            "headache": "None",
            "blurred_vision": "None",
            "convulsion": "None",
            "gcs": "15",
            "drt": "Normal",
            "uop": "Normal",
            "oxytocin_drop": "None",
            "oxytocin_dose": "None",
            "contractions": "None",
            "membranes": "Intact",
            "cervical_dilation": "3cm",
            "effacement": "50%",
            "station": "0"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_charts(self):
        url = reverse('chart-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_chart(self):
        chart = Chart.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", purpose="Test Purpose",
            blood_pressure="120/80", respiratory_rate="16", temperature="36.5",
            pulse_rate="72", spo2="98%", fetal_heart_rate="150", abdominal_pain="None",
            vaginal_bleeding="None", rash="None", itching="None", vomiting="None",
            headache="None", blurred_vision="None", convulsion="None", gcs="15",
            drt="Normal", uop="Normal", oxytocin_drop="None", oxytocin_dose="None",
            contractions="None", membranes="Intact", cervical_dilation="3cm",
            effacement="50%", station="0"
        )
        url = reverse('chart-detail', args=[chart.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_chart(self):
        chart = Chart.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", purpose="Test Purpose",
            blood_pressure="120/80", respiratory_rate="16", temperature="36.5",
            pulse_rate="72", spo2="98%", fetal_heart_rate="150", abdominal_pain="None",
            vaginal_bleeding="None", rash="None", itching="None", vomiting="None",
            headache="None", blurred_vision="None", convulsion="None", gcs="15",
            drt="Normal", uop="Normal", oxytocin_drop="None", oxytocin_dose="None",
            contractions="None", membranes="Intact", cervical_dilation="3cm",
            effacement="50%", station="0"
        )
        url = reverse('chart-detail', args=[chart.id])
        data = {"purpose": "Updated Purpose"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        chart.refresh_from_db()
        self.assertEqual(chart.purpose, "Updated Purpose")

    def test_delete_chart(self):
        chart = Chart.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", purpose="Test Purpose",
            blood_pressure="120/80", respiratory_rate="16", temperature="36.5",
            pulse_rate="72", spo2="98%", fetal_heart_rate="150", abdominal_pain="None",
            vaginal_bleeding="None", rash="None", itching="None", vomiting="None",
            headache="None", blurred_vision="None", convulsion="None", gcs="15",
            drt="Normal", uop="Normal", oxytocin_drop="None", oxytocin_dose="None",
            contractions="None", membranes="Intact", cervical_dilation="3cm",
            effacement="50%", station="0"
        )
        url = reverse('chart-detail', args=[chart.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class MedicationTests(APITestBase):
    def test_create_medication(self):
        url = reverse('medication-list')
        data = {
            "client_name": "Test Client",
            "given_by": "Test Giver",
            "dose": "500mg",
            "route": "Oral",
            "frequency": "Once daily"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_medications(self):
        url = reverse('medication-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_medication(self):
        medication = Medication.objects.create(
            client_name="Test Client", given_by="Test Giver", dose="500mg",
            route="Oral", frequency="Once daily"
        )
        url = reverse('medication-detail', args=[medication.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_medication(self):
        medication = Medication.objects.create(
            client_name="Test Client", given_by="Test Giver", dose="500mg",
            route="Oral", frequency="Once daily"
        )
        url = reverse('medication-detail', args=[medication.id])
        data = {"dose": "1000mg"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        medication.refresh_from_db()
        self.assertEqual(medication.dose, "1000mg")

    def test_delete_medication(self):
        medication = Medication.objects.create(
            client_name="Test Client", given_by="Test Giver", dose="500mg",
            route="Oral", frequency="Once daily"
        )
        url = reverse('medication-detail', args=[medication.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class OrderTests(APITestBase):
    def test_create_order(self):
        url = reverse('order-list')
        data = {
            "client_name": "Test Client",
            "ordered_by": "Test Orderer",
            "order_to": "Test Receiver",
            "order_detail": "Test Detail",
            "result": "Pending",
            "done_by": "Test Performer"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_orders(self):
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_order(self):
        order = Order.objects.create(
            client_name="Test Client", ordered_by="Test Orderer", order_to="Test Receiver",
            order_detail="Test Detail", result="Pending", done_by="Test Performer"
        )
        url = reverse('order-detail', args=[order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_order(self):
        order = Order.objects.create(
            client_name="Test Client", ordered_by="Test Orderer", order_to="Test Receiver",
            order_detail="Test Detail", result="Pending", done_by="Test Performer"
        )
        url = reverse('order-detail', args=[order.id])
        data = {"result": "Completed"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order.refresh_from_db()
        self.assertEqual(order.result, "Completed")

    def test_delete_order(self):
        order = Order.objects.create(
            client_name="Test Client", ordered_by="Test Orderer", order_to="Test Receiver",
            order_detail="Test Detail", result="Pending", done_by="Test Performer"
        )
        url = reverse('order-detail', args=[order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ConsentTests(APITestBase):
    def test_create_consent(self):
        url = reverse('consent-list')
        data = {
            "client_name": "Test Client",
            "health_pro_name": "Test Pro",
            "consent_detail": "Test Consent Detail",
            "patient_response": "Test Response"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_consents(self):
        url = reverse('consent-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_consent(self):
        consent = Consent.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", consent_detail="Test Consent Detail",
            patient_response="Test Response"
        )
        url = reverse('consent-detail', args=[consent.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_consent(self):
        consent = Consent.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", consent_detail="Test Consent Detail",
            patient_response="Test Response"
        )
        url = reverse('consent-detail', args=[consent.id])
        data = {"consent_detail": "Updated Consent Detail"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        consent.refresh_from_db()
        self.assertEqual(consent.consent_detail, "Updated Consent Detail")

    def test_delete_consent(self):
        consent = Consent.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", consent_detail="Test Consent Detail",
            patient_response="Test Response"
        )
        url = reverse('consent-detail', args=[consent.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class InterventionTests(APITestBase):
    def test_create_intervention(self):
        url = reverse('intervention-list')
        data = {
            "client_name": "Test Client",
            "health_pro_name": "Test Pro",
            "intervention_detail": "Test Intervention Detail"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_interventions(self):
        url = reverse('intervention-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_intervention(self):
        intervention = Intervention.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", intervention_detail="Test Intervention Detail"
        )
        url = reverse('intervention-detail', args=[intervention.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_intervention(self):
        intervention = Intervention.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", intervention_detail="Test Intervention Detail"
        )
        url = reverse('intervention-detail', args=[intervention.id])
        data = {"intervention_detail": "Updated Intervention Detail"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        intervention.refresh_from_db()
        self.assertEqual(intervention.intervention_detail, "Updated Intervention Detail")

    def test_delete_intervention(self):
        intervention = Intervention.objects.create(
            client_name="Test Client", health_pro_name="Test Pro", intervention_detail="Test Intervention Detail"
        )
        url = reverse('intervention-detail', args=[intervention.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)





