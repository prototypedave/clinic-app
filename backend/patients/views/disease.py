from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..serializers import DiseaseManagementSerializer
from ..models import PatientRecord


def SerializerData(data):
    return {
        "complaint" : data.get("complaint"),
        "onset" : data.get("onset"),
        "location" : data.get("location"),
        "severity" : data.get("severity"),
        "character" : data.get("character"),
        "factors" : data.get("factors"),
    }

class DiseaseRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        id = request.data.get("id")
        if not id:
            return JsonResponse({"error": "Record ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = SerializerData(request.data)

        try:
            record = PatientRecord.objects.get(id=id)
        except PatientRecord.DoesNotExist:
            return JsonResponse({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DiseaseManagementSerializer(record, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Emergency record updated successfully"}, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
