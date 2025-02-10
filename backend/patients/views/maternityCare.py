from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..serializers import MaternitySerializer
from ..models import PatientRecord


def SerializerData(data):
    return {
        "edd" : data.get("edd"),
        "gravidity" : data.get("gravidity"),
        "parity" : data.get("parity"),
        "lmp" : data.get("lmp"),
        "ppc" : data.get("ppc"),
        "pbc" : data.get("pbc"),
        "place_of_birth" : data.get("place_of_birth"),
        "pain_management" : data.get("pain_management")
    }


class MaternityCareRecordView(APIView):
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
        
        serializer = MaternitySerializer(record, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Emergency record updated successfully"}, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)