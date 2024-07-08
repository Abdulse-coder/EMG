from django.db import models

class PharmacyOrder(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    patient_name = models.CharField(max_length=50)
    health_provider_name = models.CharField(max_length=50)
    pharmacist_name = models.CharField(max_length=50)
    drug_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    full_order_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_number} - {self.patient_name}"

