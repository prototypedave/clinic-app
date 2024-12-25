from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AdminRegistrationSerializer

class AdminRegistrationView(APIView):
    def post(self, request):
        serializer = AdminRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Admin registered successfully!"}, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Admin already exists, Please try logging in",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
