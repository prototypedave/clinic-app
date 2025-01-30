from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Patient
from .serializers import PatientSerializer, DependantSerializer, RecordSerializer


def get_convert_request_to_patient_object(request):
    """
        Retrieves and returns 
    """

class RegisterPatient(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # if request is valid
        if request.data:
            # check if its parent
            if request.data.get('guardian'):
                parent_data = {
                    "first_name" : request.data.get("g_first"),
                    "middle_name" : request.data.get("g_middle"),
                    "last_name" : request.data.get("g_last"),
                    "mobile" : request.data.get("mobile"),
                    "age" : request.data.get("g_dob"),
                    "address" : request.data.get("address"),
                    "guardian" : request.data.get("guardian"),
                    "family_history" : request.data.get("family_history"),
                    "gender" : request.data.get("gender"),
                    "email" : request.data.get("email")
                }

                parent = PatientSerializer(data=parent_data)
                if parent.is_valid():
                    parent_instance = parent.save()
                    dependant_data = {
                        "guardian" : parent_instance.id,
                        "first_name" : request.data.get("first"),
                        "middle_name" : request.data.get("middle"),
                        "last_name" : request.data.get("last"),
                        "age": request.data.get("dob"),
                        "gender": request.data.get("gender")
                    }

                    dependant = DependantSerializer(data=dependant_data)
                    if dependant.is_valid():
                        instance = dependant.save()
                        record_data = {
                            "dependant" : instance.id,
                            "reason" : request.data.get("reason")
                        }

                        record = RecordSerializer(data=record_data)
                        if record.is_valid():
                            record.save()
                            return JsonResponse({"message": "Patient Registered Successfully"}, status=status.HTTP_200_OK)
                        return JsonResponse({"error": "Invalid Reason Data"}, status=status.HTTP_400_BAD_REQUEST)
                    return JsonResponse({"error": "Invalid Patient Details"}, status=status.HTTP_400_BAD_REQUEST)
                return JsonResponse({"error" : "Invalid Guardian Details"}, status=status.HTTP_400_BAD_REQUEST)
            
            patient_data = {
                "first_name" : request.data.get("first"),
                "middle_name" : request.data.get("middle"),
                "last_name" : request.data.get("last"),
                "mobile" : request.data.get("mobile"),
                "age" : request.data.get("dob"),
                "address" : request.data.get("address"),
                "guardian" : request.data.get("guardian"),
                "family_history" : request.data.get("family_history"),
                "gender" : request.data.get("gender"),
                "email" : request.data.get("email")
            }
            
            patient = PatientSerializer(data=patient_data)
            if patient.is_valid():
                instance = patient.save()
                record_data = {
                    "patient" : instance.id,
                    "reason" : request.data.get("reason")
                }

                record = RecordSerializer(data=record_data)
                if record.is_valid():
                    record.save()
                    return JsonResponse({"message": "Patient Registered Successfully"}, status=status.HTTP_201_OK)
                return JsonResponse({"error": "Invalid Reason Data"}, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({"error": "Invalid Patient Details"}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

        