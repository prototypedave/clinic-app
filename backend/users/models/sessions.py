"""from django.db import models
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken
from django.utils.timezone import now
from datetime import timedelta

class UserSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='session')
    token = models.OneToOneField(AccessToken, on_delete=models.CASCADE, null=True, blank=True)
    last_activity = models.DateTimeField(auto_now=True)


    def is_inactive(self):
        return self.last_activity < now() - timedelta(hours=1)
"""