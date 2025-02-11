from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..serializers import RehabilitationSerializer
from ..models import PatientRecord


def SerializerData(data):
    return {
        "diagnosis" : data.get("diagnosis"),
        "injury_date" : data.get("doi"),
        "injury_type" : data.get("type"),
    }


class RehabilitationRecordView(APIView):
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
        
        serializer = RehabilitationSerializer(record, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Data saved successfully"}, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)