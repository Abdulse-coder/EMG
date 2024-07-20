from rest_framework import serializers
from .models import WardAdmissionDischarge

class WardAdmissionDischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardAdmissionDischarge
        fields = '__all__'