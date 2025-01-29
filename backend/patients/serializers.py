from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Patient, PatientRecord, PatientDependant

class PatientSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = [
            "first_name", "middle_name", "last_name", "mobile", "age", "address", "guardian", "family_history",
            "gender", "email"
        ]

    def get_gender(self, obj):
        return obj.get_gender_display()
    
    def to_internal_value(self, data):
        """ Convert 'Male'/'Female' input to 'M'/'F' before saving """
        gender_mapping = {"Male": "M", "Female": "F", "male": "M", "female": "F"}
        data['gender'] = gender_mapping.get(data.get('gender'), data.get('gender'))
        return super().to_internal_value(data)


class DependantSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()

    class Meta:
        model = PatientDependant
        fields = [
            "guardian", "first_name", "last_name", "age", "gender"
        ]

    def get_gender(self, obj):
        return obj.get_gender_display()
    
    def to_internal_value(self, data):
        """ Convert 'Male'/'Female' input to 'M'/'F' before saving """
        gender_mapping = {"Male": "M", "Female": "F", "male": "M", "female": "F"}
        data['gender'] = gender_mapping.get(data.get('gender'), data.get('gender'))
        return super().to_internal_value(data)