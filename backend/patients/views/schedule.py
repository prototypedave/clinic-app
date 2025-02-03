from django.http import JsonResponse
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models import PatientRecord, PatientDependant
from ..serializers import AppointmentRecordSerializer
import requests
from django.conf import settings

class SchedulePatientView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        appoint_ser = {
            "appointment": request.data.get('reason')
        }
        record_id = request.data.get("id")
        token = request.auth.token

        try:
            record = PatientRecord.objects.get(id=record_id)
        except PatientRecord.DoesNotExist:
            return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

        patient_id = record.get_patient()

        if patient_id is not None:
            parent = patient_id.get('patient')
            if patient_id.get('model') == "dependant":
                # Retrieve parent details
                try:
                    parent = PatientDependant.objects.get(id=patient_id.get('patient').id)
                except PatientRecord.DoesNotExist:
                    return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

            email = parent.email if parent.email else settings.EMAIL_HOST_USER

            data = {
                "first_name": parent.first_name,
                "middle_name": parent.middle_name,
                "last_name": parent.last_name,
                "mobile": parent.mobile,
                "email": email,
                "reason": request.data.get("reason"),
                "title": request.data.get("type"),
                "start": request.data.get('start'),
                "end": request.data.get('end'),
            }

            with transaction.atomic():
                api_url = f"{settings.BASE_URL}/appointments/add-appointment"
                headers = {
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json'
                }

                response = requests.post(api_url, json=data, headers=headers)

                if response.status_code == 201:
                    record = AppointmentRecordSerializer(record, data=appoint_ser, partial=True)
                    if record.is_valid():
                        record.save()
                        return JsonResponse({"message": "Appointment booked successfully"}, status=status.HTTP_201_CREATED)
                    else:
                        transaction.set_rollback(True)
                        return JsonResponse({"error": "Validation failed", "details": record.errors}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    transaction.set_rollback(True)
                    return JsonResponse({"error": "Failed to book appointment", "details": response.json()}, status=response.status_code)

        return JsonResponse({"error": "Something went wrong, patient not found"}, status=status.HTTP_400_BAD_REQUEST)