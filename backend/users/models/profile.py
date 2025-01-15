"""from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_image = models.ImageField(
        upload_to="profile_images/",
        default="profile_images/default.png",  
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
"""