from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from oauth2_provider.models import AccessToken, RefreshToken, Application
from oauthlib.common import generate_token
from django.utils.timezone import now
from datetime import timedelta
from ..models import UserSession

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(username=email, password=password)
        if user:
            application, _ = Application.objects.get_or_create(
                user=user,
                client_type=Application.CLIENT_CONFIDENTIAL,
                authorization_grant_type=Application.GRANT_PASSWORD,
                defaults={"name": "Default Application"}
            )

            # Create access and refresh tokens
            expires = now() + timedelta(seconds=3600)  # Set token expiration (1 hour)
            access_token = AccessToken.objects.create(
                user=user,
                scope="read write",
                expires=expires,
                token=generate_token(),
                application=application,
            )
            
            refresh_token = RefreshToken.objects.create(
                user=user,
                token=generate_token(),
                application=application,
                access_token=access_token,
            )

            # Manage user session
            session, created = UserSession.objects.get_or_create(user=user)
            if created or session.is_inactive():
                if not created and session.token:
                    session.token.delete()
                session.token = access_token
                session.save()
            else:
                session.token = access_token
                session.save()

            # Return tokens in the response
            return Response({
                'access_token': access_token.token,
                'refresh_token': refresh_token.token,
                'expires_in': 3600, 
                'token_type': 'Bearer',
                'message': 'Login successful',
            })

        return Response({'error': 'Invalid username or password'}, status=401)
