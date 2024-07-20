from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WardAdmissionDischargeViewSet

router = DefaultRouter()
router.register(r'ward-admissions', WardAdmissionDischargeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
