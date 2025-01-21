from .models import Appointments
from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ["start", "end", "title", "reason", "first_name", "middle_name", "last_name", "mobile", "email"]
    

class RescheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ["start", "end", "reschedule_reason"]
