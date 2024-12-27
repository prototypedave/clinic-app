from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import UserSession

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                user_session = UserSession.objects.get(user=request.user)
                
                if user_session.is_inactive():
                    user_session.token.delete()  
                    user_session.delete()        
                    return JsonResponse({'error': 'Session expired due to inactivity'}, status=401)
                
                user_session.last_activity = timezone.now()
                user_session.save()

            except UserSession.DoesNotExist:
                pass
        
        response = self.get_response(request)
        return response
