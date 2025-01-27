from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicineSerializer
from .models import Medicine

class AddMedicineView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.data:
            medicine = MedicineSerializer(request.data)
            if medicine.is_valid():
                medicine.save()
                return JsonResponse({"message": "Medicine saved Successfully"}, status=201)
            return JsonResponse({"error": "Invalid fields. Please try again"}, status=400)
        return JsonResponse({"error": "Empty or invalid response to server"}, status=400)
    

class NotifyExpiry(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        medicine = Medicine.objects.almost_expired(request.data.get("num_days"))
        medicine_list = [{
            "name": med.name,
            "lot": med.batch_number,
            "qty": med.quantity,
        } for med in medicine]
        return JsonResponse({"med" : medicine_list}, status=201)