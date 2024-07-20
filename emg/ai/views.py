from rest_framework import viewsets, permissions
from .models import Access, Recommadtion
from .serializers import AccessSerializer, RecommadtionSerializer

class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecommadtionViewSet(viewsets.ModelViewSet):
    queryset = Recommadtion.objects.all()
    serializer_class = RecommadtionSerializer
    permission_classes = [permissions.IsAuthenticated]
