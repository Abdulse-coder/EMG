from django.db import models

# Create your models here.

class Access(models.Model):
    accessed_card = models.CharField(max_length=200)
    accessed_by = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_abnormal = models.BooleanField(default=False)
class Recommadtion(models.Model):
    client_name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    recommadtion = models.TextField(default="empty")
    education = models.TextField(default="empty")


