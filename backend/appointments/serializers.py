from .models import Appointments
from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ["start", "end", "title", "reason", "patientId"]
    

class RescheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ["start", "end", "reschedule_reason"]
