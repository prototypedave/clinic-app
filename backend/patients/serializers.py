from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Patient, PatientRecord

class PatientCheckUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "first_name", "middle_name", "last_name", "mobile",
        ]


class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = [
            "patient", "reason",
        ]