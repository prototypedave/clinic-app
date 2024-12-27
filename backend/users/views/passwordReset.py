from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.mail import send_mail
import uuid
from django.utils.timezone import now

RESET_TOKEN_EXPIRATION = 5 * 60  # 5 minutes

class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            
            # Generate a unique token
            token = str(uuid.uuid4())
            
            # Store the token with the email and timestamp in the cache
            token_info = {
                'email': user.email,
                'created_at': now()
            }
            cache.set(token, token_info, timeout=RESET_TOKEN_EXPIRATION)

            # Construct the reset link
            reset_link = f'http://localhost:8080/change-password/{token}'

            # Send the email
            send_mail(
                'Password Reset Request',
                f'Follow this link to reset your password: {reset_link}',
                'popupgfj@gmail.com',
                [user.email],
                fail_silently=False,
            )

            return Response({'message': 'Password reset email sent'})
        
        except User.DoesNotExist:
            return Response({'error': 'Email not found'}, status=404)
