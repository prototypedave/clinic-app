from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializer import AdminRegistrationSerializer, ResetPasswordSerializer
import logging, uuid
from django.core.cache import cache
from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.conf import settings

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
    
   
RESET_TOKEN_EXPIRATION = 5 * 60

class SendResetLinkView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            token = str(uuid.uuid4())   
            # Store the token with the email and timestamp in the cache
            token_info = {
                'email': user.email,
                'created_at': now()
            }
            cache.set(token, token_info, timeout=RESET_TOKEN_EXPIRATION)
            reset_link = f'{settings.FRONTEND_ADDRESS}/change-password/{token}'

            # Send the email
            send_mail(
                'Password Reset Request',
                f'Follow this link to reset your password: {reset_link}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return Response({'message': 'Password reset email sent'})
        
        except User.DoesNotExist:
            return Response({'error': 'Email not found'}, status=404)

RESET_TOKEN = timedelta(minutes=5)     

class ResetTokenValidationView(APIView):
    def get(self, request, token):
        token_info = cache.get(token)

        if token_info:
            token_creation_time = token_info.get('created_at')
            if token_creation_time and now() < token_creation_time + RESET_TOKEN:
                return Response({'valid': True, 'email': token_info['email']}, status=status.HTTP_200_OK)
            else:
                cache.delete(token)
        
        return Response({'valid': False, 'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)


class ValidView(APIView):
    def get(self, request, token):
        token_info = cache.get(token)
        if token_info:
            token_creation_time = token_info.get('created_at')
            if token_creation_time and now() < token_creation_time + RESET_TOKEN_EXPIRATION:
                return JsonResponse({'valid': True})  
        return JsonResponse({'valid': False, 'error': 'Invalid or expired token'})


class PasswordResetView(APIView):
    def post(self, request, token):
        token_info = cache.get(token)
        if not token_info:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

        # check password and confirmation)
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
            cache.delete(token)

            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)