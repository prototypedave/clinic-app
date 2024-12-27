from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.core.cache import cache
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now, timedelta
from django.http import JsonResponse

RESET_TOKEN_EXPIRATION = timedelta(minutes=5)

class PasswordResetTokenValidationView(APIView):
    def get(self, request, token):
        token_info = cache.get(token)

        if token_info:
            token_creation_time = token_info.get('created_at')
            if token_creation_time and now() < token_creation_time + RESET_TOKEN_EXPIRATION:
                return Response({'valid': True, 'email': token_info['email']}, status=status.HTTP_200_OK)
            else:
                cache.delete(token)
        
        return Response({'valid': False, 'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetValidView(APIView):
    def get(self, request, token):
        token_info = cache.get(token)
        if token_info:
            token_creation_time = token_info.get('created_at')
            if token_creation_time and now() < token_creation_time + RESET_TOKEN_EXPIRATION:
                return JsonResponse({'valid': True})  
        return JsonResponse({'valid': False, 'error': 'Invalid or expired token'})


class PasswordUpdateView(APIView):
    def post(self, request, token):
        # Get the token info from cache
        token_info = cache.get(token)
        print(token)
        if not token_info:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

        # Additional validation (e.g., check password and confirmation)
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        if len(password) < 8:
            return Response({'error': 'Password must be at least 8 characters long'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the password for the user
        email = token_info['email']
        try:
            user = User.objects.get(email=email)
            user.password = make_password(password)
            user.save()

            # Delete the token from the cache after use
            cache.delete(token)

            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
