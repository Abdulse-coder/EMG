from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccessViewSet, RecommadtionViewSet

router = DefaultRouter()
router.register(r'accesses', AccessViewSet)
router.register(r'recommadtions', RecommadtionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
