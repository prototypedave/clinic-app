from .models import Expense
from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["purpose", "amount", "notes", "date", "reported_by"]