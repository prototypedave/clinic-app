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
            medicine = MedicineSerializer(data=request.data)
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
        medicines = request.data.get('medicine')

        if not medicines or not isinstance(medicines, list):
            return JsonResponse({'error': "Check every field is submitted correctly"}, status=status.HTTP_400_BAD_REQUEST)
        
        results = []
        for medicine_data in medicines:
            name = medicine_data.get('name')
            batch_number = medicine_data.get('batch_number')
            quantity_to_use = medicine_data.get('quantity')
            strength = medicine_data.get('strength')
            manufacturer = medicine_data.get('manufacturer')

            if not name or not batch_number or quantity_to_use is None:
                results.append({'error': 'Name, batch number, and quantity are required.', 'medicine': medicine_data})
                continue

            if not name or not batch_number or quantity_to_use is None:
                results.append({'error': 'Name, batch number, and quantity are required.', 'medicine': medicine_data})
                continue

            # Get the closest batch number
            closest_batch = Medicine.objects.get_batch_number_of_given_medicine(
                name=name, strength=strength, manufacturer=manufacturer
            )

            if closest_batch is None:
                results.append({'error': 'No medicines registered with the given name.', 'medicine': medicine_data})
                continue

            if batch_number != closest_batch:
                results.append({
                    'error': f"Please provide the batch number: {closest_batch}, which is closest to expiry.",
                    'medicine': medicine_data
                })
                continue

            try:
                medicine = Medicine.objects.get(name=name, batch_number=batch_number)
            except Medicine.DoesNotExist:
                results.append({'error': 'The provided batch number is not yet registered.', 'medicine': medicine_data})
                continue

            if quantity_to_use > medicine.quantity:
                results.append({'error': 'Insufficient quantity available.', 'medicine': medicine_data})
                continue

            medicine.quantity -= quantity_to_use
            medicine.save()

        if results:
            return JsonResponse({"error": results}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({'message': 'Success'}, status=status.HTTP_200_OK)
    

class MedicineCost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        batches = request.data.get('batch')

        if not batches or not isinstance(batches, list):
            return JsonResponse({'error': "List cannot be empty or invalid list"}, status=status.HTTP_400_BAD_REQUEST)
        
        total = []
        for batch in batches:
            try:
                medicine = Medicine.objects.get(batch_number=batch.get('batch_number'))
                med = {
                    "name": medicine.name,
                    "batch": medicine.batch_number,
                    "qty": batch.get('quantity'),
                    "cost": medicine.get_price(batch.get('quantity')),
                }
                total.append(med)
            except Medicine.DoesNotExist:
                total.append(None)
        
        if total:
            return JsonResponse({'costs': total}, status=status.status.HTTP_201_OK)
        return JsonResponse({'error': "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
            

