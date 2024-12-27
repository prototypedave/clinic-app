from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from datetime import timedelta
from django.utils import timezone

class UserSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.OneToOneField(Token, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(auto_now=True)
    
    def is_inactive(self):
        return timezone.now() - self.last_activity > timedelta(minutes=10)
    
    def __str__(self):
        return f"Session for {self.user.email}"
