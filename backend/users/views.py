from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializer import AdminRegistrationSerializer
import logging

logger = logging.getLogger(__name__)


class SuperuserCheckView(APIView):
    def get(self, request):
        # Check if a superuser exists
        superuser_exists = User.objects.filter(is_superuser=True).exists()
        return Response({"superuser_exists": superuser_exists}, status=status.HTTP_200_OK)
    

class AdminRegistrationView(APIView):
    def post(self, request):
        logger.info(f"Received data: {request.data}")
        serializer = AdminRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Admin registered successfully!"}, status=status.HTTP_201_CREATED)

        logger.error(f"Validation errors: {serializer.errors}")
        return Response({
            "message": "Admin already exists, Please try logging in",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)