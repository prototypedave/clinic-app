from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.urls import reverse
from ..serializer import ProfileImageSerializer

class UpdateProfileImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = ProfileImageSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile image updated successfully."})
        return Response(serializer.errors, status=400)
   

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'email': user.email,
            'name': user.get_full_name(),
            'avatar': request.build_absolute_uri(user.get_avatar()),
            'title': user.get_title()
        })