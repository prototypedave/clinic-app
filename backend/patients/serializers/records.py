from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import PatientRecord


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = [
            "patient", "dependant", "reason", 
        ]


class EmergencyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = [
            "complaint", "onset", "location", "severity",
            "character", "factors"
        ]


class AppointmentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = [
            "appointment"
        ]