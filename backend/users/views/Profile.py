"""from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Profile
from ..serializer import ProfileImageSerializer
from django.conf import settings
from django.urls import reverse

class UpdateProfileImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        profile = request.user.profile
        serializer = ProfileImageSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile image updated successfully."})
        return Response(serializer.errors, status=400)
    

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            user_profile = Profile.objects.get(user=user)
            profile_image_url = user_profile.profile_image.url
        except Profile.DoesNotExist:
            profile_image_url = settings.MEDIA_URL + 'profile_images/default.png'
        return Response({
            'email': user.email,
            'name': user.get_full_name(),
            'profile_image': request.build_absolute_uri(profile_image_url),
        })
"""