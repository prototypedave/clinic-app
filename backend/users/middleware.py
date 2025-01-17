from datetime import timedelta
from django.utils.timezone import now
from .models import UserSession

class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            session = UserSession.objects.filter(user=request.user).first()
            if session:
                timeout = timedelta(minutes=30)  
                if now() - session.last_activity > timeout:
                    session.token.delete()  
                else:
                    session.last_activity = now()
                    session.save()

        return self.get_response(request)
