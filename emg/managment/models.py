from django.db import models

class WardAdmissionDischarge(models.Model):
    patient_name = models.CharField(max_length=100, blank=False, null=False)
    admission_date = models.DateTimeField(auto_now_add=True)
    admitted_by = models.CharField(max_length=100, blank=False, null=False)
    ward_name = models.CharField(max_length=100, blank=False, null=False)
    discharged_by = models.CharField(max_length=100, blank=False, null=False)
    discharged_from_hospital = models.BooleanField(default=False)
    discharge_remark = models.TextField(blank=False, null=False)
    discharge_date = models.DateTimeField(blank=False, null=False)
    appointment = models.CharField(max_length=100, blank=False, null=False)

    

    