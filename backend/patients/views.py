from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Patient
from .serializers import PatientCheckUpSerializer, PatientReasonSerializer


class CheckRegisteredPatient(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # if request is valid
        if request.data:
            mobile = request.data.get('mobile')
            if mobile:
                # retrieve patient instance registered with this mobile if present
                pk = Patient.objects.check_if_patient_exists(mobile)
                if pk is not None:
                    # update patient record
                    ser_data = {
                        "patient" : pk,
                        "reason" : request.data.get('reason'),
                    }
                    record = PatientReasonSerializer(data=ser_data)
                    if record.is_valid():
                        record.save()
                        return JsonResponse({"registered" : True}, status=status.HTTP_200_OK)
                    return JsonResponse({"error" : "client is registered but invalid fields are provided"}, status=401)
                
                # new patient
                ser_data = {
                    "first_name": request.data.get('first'),
                    "middle_name": request.data.get('second'),
                    "last_name": request.data.get('last'),
                    "mobile": mobile,
                }
                patient = PatientCheckUpSerializer(data=ser_data)
                if patient.is_valid():
                    patient.save()
                    pk = Patient.objects.check_if_patient_exists(mobile)
                    ser_data = {
                        "patient" : pk,
                        "reason" : request.data.get('reason'),
                    }
                    record = PatientReasonSerializer(data=ser_data)
                    if record.is_valid():
                        record.save()
                        return JsonResponse({"registered" : False}, status=status.HTTP_200_OK)
                    return JsonResponse({"error" : "client is registered but invalid fields are provided"}, status=401)
                