from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicineSerializer
from .models import Medicine
from rest_framework import status
from rest_framework.exceptions import ValidationError

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
    

class UpdateMedicineUse(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = request.data.get('name')
        batch_number = request.data.get('batch_number')
        quantity_to_use = request.data.get('quantity')
        strength = request.data.get('strength')
        manufacturer = request.data.get('manufacturer')

        if not name or not batch_number or quantity_to_use is None:
            return JsonResponse({'error': 'Name, batch number, and quantity are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        closest_batch = Medicine.objects.get_batch_number_of_given_medicine(name=name, strength=strength, manufacturer=manufacturer)
        
        if closest_batch is None:
            return JsonResponse({'error': 'No medicines registered with the given name.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if batch_number != closest_batch:
            return JsonResponse({'error': f"Please give the batch number: {closest_batch}, which is closest to expiry."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            medicine = Medicine.objects.get(name=name, batch_number=batch_number)
        except Medicine.DoesNotExist:
            return JsonResponse({'error': 'The provided batch number is not yet registered.'}, status=status.HTTP_404_NOT_FOUND)

        if quantity_to_use > medicine.quantity:
            return JsonResponse({'error': 'Insufficient quantity available.'}, status=status.HTTP_400_BAD_REQUEST)

        medicine.quantity -= quantity_to_use
        medicine.save()

        return JsonResponse({'message': f'Successfully updated the quantity. Remaining quantity: {medicine.quantity}'}, status=status.HTTP_200_OK)

