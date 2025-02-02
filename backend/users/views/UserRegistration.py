from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
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
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.signing import TimestampSigner, SignatureExpired, BadSignature
from django.utils.http import urlsafe_base64_decode
from django.views import View
import json

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
    

signer = TimestampSigner()

class SendResetLinkView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = signer.sign(uid) 
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
        try:
            # Attempt to decode and validate the token
            uid = signer.unsign(token, max_age=300)  
            user_id = urlsafe_base64_decode(uid).decode("utf-8")

            # If the user exists, return success
            user = User.objects.get(pk=user_id)
            return JsonResponse({"valid": True, "message": "Token is valid", "user_id": user.id}, status=200)

        except SignatureExpired:
            # Handle expired tokens specifically
            cache.delete(token)  
            return JsonResponse({"valid": False, "error": "Token has expired"}, status=400)

        except BadSignature:
            # Handle invalid tokens
            cache.delete(token)
            return JsonResponse({"valid": False, "error": "Invalid token"}, status=400)

        except User.DoesNotExist:
            # Handle case when user does not exist
            return JsonResponse({"valid": False, "error": "User not found"}, status=404)

        except Exception as e:
            # Handle unexpected errors
            return JsonResponse({"valid": False, "error": "Unexpected error", "details": str(e)}, status=500)


class InvalidateTokenView(APIView):
    def delete(self, request, token):
        # Delete token from cache
        if cache.get(token):
            cache.delete(token)
            return JsonResponse({"message": "Token invalidated successfully"}, status=200)
        return JsonResponse({"error": "Token not found or already expired"}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class PasswordResetView(APIView):
    def post(self, request, token):
        try:
            uid = signer.unsign(token, max_age=300)  
            user_id = urlsafe_base64_decode(uid).decode("utf-8")
            user = User.objects.get(pk=user_id)

            new_password = request.data.get("password")
            if new_password:
                user.set_password(new_password)
                user.save()
                return JsonResponse({'message': 'Password reset successful'}, status=200)
            return JsonResponse({'error': 'New password not provided'}, status=400)
        except SignatureExpired:
            return JsonResponse({'error': 'Token has expired'}, status=400)
        except (BadSignature, User.DoesNotExist):
            return JsonResponse({'error': 'Invalid token'}, status=400)
        