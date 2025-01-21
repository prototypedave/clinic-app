from .models import Medicine
from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'name', 'manufacturer', 'category', 'dosage_quantity', 'strength',
            'dosage_form', 'price', 'stock', 'expiry_date', 'received_date',
            'ordered_date', 'buy_price'
        ]