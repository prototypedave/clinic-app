from .models import Medicine
from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'name', 'batch_number', 'expiry_date', 'quantity', 'cost', 'price',
            'type', 'administration', 'strength', 'manufacturer', 'supplier'
        ]