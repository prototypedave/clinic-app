from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import DiseaseManagementRecord


class DiseaseManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseManagementRecord
        fields = [
            "diagnosis", "dod", "smoking", "severity", "alcohol", "physical", "diet"
        ]