from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Medicine, MedicineHistory
from .serializers import MedicineSerializer  

class AddMedicineView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        serializer = MedicineSerializer(data=data)
        if not serializer.is_valid():
            return JsonResponse({"error": serializer.errors}, status=400)

        validated_data = serializer.validated_data

        unique_fields = {
            'name': validated_data['name'],
            'manufacturer': validated_data['manufacturer'],
            'category': validated_data['category'],
            'dosage_quantity': validated_data['dosage_quantity'],
            'strength': validated_data['strength'],
            'dosage_form': validated_data['dosage_form'],
        }
        
        try:
            existing_medicine = Medicine.objects.get(**unique_fields)
            MedicineHistory.objects.create(
                medicine=existing_medicine,
                name=existing_medicine.name,
                manufacturer=existing_medicine.manufacturer,
                category=existing_medicine.category,
                dosage_quantity=existing_medicine.dosage_quantity,
                strength=existing_medicine.strength,
                dosage_form=existing_medicine.dosage_form,
                price=existing_medicine.price,
                stock=existing_medicine.stock,
                expiry_date=existing_medicine.expiry_date,
            )

            for field, value in validated_data.items():
                setattr(existing_medicine, field, value)
            existing_medicine.save()

            return JsonResponse({"message": "Medicine updated successfully"}, status=200)

        except Medicine.DoesNotExist:
            Medicine.objects.create(**validated_data)
            return JsonResponse({"message": "New medicine added successfully"}, status=201)
