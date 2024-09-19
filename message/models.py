from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.CharField(max_length=200)
    sent_on = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_on']

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient}"