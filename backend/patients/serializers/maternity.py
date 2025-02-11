from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import MaternityCareRecord


class MaternitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaternityCareRecord
        fields = [
            "edd", "gravidity", "parity", "lmp", "ppc", "pbc", "place_of_birth", "pain_management"
        ]