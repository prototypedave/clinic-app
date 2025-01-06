from django.urls import path

from . import views

urlpatterns = [
    path("admin-registration", views.AdminRegistrationView.as_view(), name='admin-register'),
    path('superuser-check/', views.SuperuserCheckView.as_view(), name='superuser-check'),
]