from django.http import JsonResponse
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
        "family_history" : data.get("family_history"),
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

    def post(self, request):
        req_data = request.data

        # Check if request is valid
        if req_data:
            patient_data = convert_request_to_patient_object(req_data)

            # Register patient
            patient = PatientSerializer(data=patient_data)
            if patient.is_valid():
                instance = patient.save()

                # Check if the patient is a dependant and save patient to Dependant instead
                if req_data.get("guardian"):
                    dependant_data = retrieve_dependant_data(data=req_data, id=instance.id)
                    dependant = DependantSerializer(data=dependant_data)
                    if dependant.is_valid():
                        instance = dependant.save()
                        record_data = {
                            "dependant" : instance.id,
                            "reason" : request.data.get("reason")
                        }

                        # Create new record for this visitation
                        record = RecordSerializer(data=record_data)
                        if record.is_valid():
                            record.save()
                            return JsonResponse({"message": "Patient Registered Successfully"}, status=status.HTTP_201_OK)
                        return JsonResponse({"error": "Error Saving Patient Record Information"}, status=status.HTTP_400_BAD_REQUEST)
                    return JsonResponse({"error": "Error Saving Dependant Details"}, status=status.HTTP_400_BAD_REQUEST)
                
                # if not continue with patient record
                record_data = {
                    "patient" : instance.id,
                    "reason" : request.data.get("reason")
                }

                # Create new record for this visitation
                record = RecordSerializer(data=record_data)
                if record.is_valid():
                    record.save()
                    return JsonResponse({"message": "Patient Registered Successfully"}, status=status.HTTP_201_OK)
                return JsonResponse({"error": "Error Saving Patient Record Information"}, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({"error": "Error Saving Patient Details"}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
            