from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import RehabilitationRecord

class RehabilitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RehabilitationRecord
        fields = [
            "diagnosis", "injury_date", "injury_type"
        ]