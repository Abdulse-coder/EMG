from rest_framework import viewsets, permissions
from .models import WardAdmissionDischarge
from .serializers import WardAdmissionDischargeSerializer

class WardAdmissionDischargeViewSet(viewsets.ModelViewSet):
    queryset = WardAdmissionDischarge.objects.all()
    serializer_class = WardAdmissionDischargeSerializer
    permission_classes = [permissions.IsAuthenticated]