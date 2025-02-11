from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import Patient
from django.db import models


class PatientSerializer(serializers.ModelSerializer):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    gender = serializers.ChoiceField(choices=GenderChoices.choices)

    class Meta:
        model = Patient
        fields = [
            "first_name", "middle_name", "last_name", "mobile", "age", "address", "guardian", "family_history",
            "gender", "email"
        ]