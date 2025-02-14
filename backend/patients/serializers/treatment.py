from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import TreatmentPlanModel


class TreatmentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentPlanModel
        fields = [
            'plan', 'diagnosis', 'medication'
        ]