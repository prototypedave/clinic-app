from django.http import JsonResponse
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import PatientSerializer, DependantSerializer, RecordSerializer


def convert_request_to_patient_object(data):
    """
        Retrieves and returns patient details in object format
    """
    return {
        "first_name" : data.get("first"),
        "middle_name" : data.get("middle"),
        "last_name" : data.get("last"),
        "mobile" : data.get("mobile"),
        "age" : data.get("dob"),
        "address" : data.get("address"),
        "guardian" : data.get("guardian"),
        "family_history" : data.get("history"),
        "gender" : data.get("gender"),
        "email" : data.get("email")
    }


def retrieve_dependant_data(data, id):
    """
        Retrieves and returns dependant details in object format
    """
    return {
        "guardian" : id,
        "first_name" : data.get("d_first"),
        "middle_name" : data.get("d_middle"),
        "last_name" : data.get("d_last"),
        "age": data.get("d_dob"),
        "gender": data.get("d_gender")
    }


class RegisterPatient(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        req_data = request.data

        if not req_data:
            return JsonResponse({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            patient_data = convert_request_to_patient_object(req_data)
            patient = PatientSerializer(data=patient_data)

            if not patient.is_valid():
                return JsonResponse({"error": "Error Saving Patient Details", "details": patient.errors}, status=status.HTTP_400_BAD_REQUEST)

            instance = patient.save()

            # Check if the patient is a dependant
            if req_data.get("guardian"):
                dependant_data = retrieve_dependant_data(data=req_data, id=instance.id)
                dependant = DependantSerializer(data=dependant_data)

                if not dependant.is_valid():
                    raise ValueError("Error Saving Dependant Details", dependant.errors)

                dependant_instance = dependant.save()
                record_data = {
                    "dependant": dependant_instance.id,
                    "reason": req_data.get("reason")
                }
            else:
                record_data = {
                    "patient": instance.id,
                    "reason": req_data.get("reason"),
                    "dependant": None
                }

            # Create a new record
            record = RecordSerializer(data=record_data)
            if not record.is_valid():
                raise ValueError("Error Saving Patient Record Information", record.errors)

            record.save()

            return JsonResponse({"message": "Patient Registered Successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            transaction.set_rollback(True)  # Ensures rollback of all saved objects
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)