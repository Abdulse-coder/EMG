from rest_framework import serializers
from .models import Access, Recommadtion

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'

class RecommadtionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommadtion
        fields = '__all__'
