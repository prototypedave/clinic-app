from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..serializers import TreatmentPlanSerializer
from ..models import PatientRecord


class TreatmentPlanView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        id = request.data.get("id")
        if not id:
            return JsonResponse({"error": "Record ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            record = PatientRecord.objects.get(id=id)
        except PatientRecord.DoesNotExist:
            return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data.pop("id", None)
        
        serializer = TreatmentPlanSerializer(data=data)  
        if serializer.is_valid():
            instance = serializer.save()
            record.treatment = instance
            record.save()
            return JsonResponse({"message": "Data saved successfully"}, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)