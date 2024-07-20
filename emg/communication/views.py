from rest_framework import viewsets, permissions
from .models import Communication
from .serializers import CommunicationSerializer

class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    permission_classes = [permissions.IsAuthenticated]
