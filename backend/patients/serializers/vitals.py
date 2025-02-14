from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import VitalsModel


class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalsModel
        fields = [
            'temperature', 'pulse', 'blood_pressure', 'respiratory_rate',
            'weight', 'height', 'neurological', 'respiratory', 'cardiovascular', 'gastrointenstinal',
            'musculoskeleton', 'skin', 'pyschological', 'pain', 'fall_risl'
        ]