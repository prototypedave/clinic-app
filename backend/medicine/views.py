from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
 

class AddMedicineView(APIView):
    permission_classes = [IsAuthenticated]

    