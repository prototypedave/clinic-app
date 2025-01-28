from django.urls import path
from . import views

urlpatterns = [
    path("check-patient", views.CheckRegisteredPatient.as_view(), name="check-patient")
]