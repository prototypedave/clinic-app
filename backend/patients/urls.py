from django.urls import path
from . import views

urlpatterns = [
    path("register-patient", views.RegisterPatient.as_view(), name="new-patient"),
    path("emergency-record", views.EmergencyRecordView.as_view(), name="emergency")
]