from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Patient
from .serializers import PatientCheckUpSerializer


class CheckRegisteredPatient(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # if request is valid
        if request.data:
            mobile = request.data.get('mobile')