from django.urls import path
from .views import AdminRegistrationView

urlpatterns = [
    path('register/', AdminRegistrationView.as_view(), name='admin-register'),
]
