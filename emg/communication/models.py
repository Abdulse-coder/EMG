# communication/models.py
from django.db import models

class Communication(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} to {self.receiver} - {self.subject}"

    class Meta:
        ordering = ['-timestamp']
