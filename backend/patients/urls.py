from django.urls import path
from . import views

urlpatterns = [
    path("register-patient", views.RegisterPatient.as_view(), name="new-patient"),
    path("emergency-record", views.EmergencyRecordView.as_view(), name="emergency"),
    path("appointment-record", views.SchedulePatientView.as_view(), name="patient-appointments"),
    path("disease-management-record", views.DiseaseRecordView.as_view(), name="disease-management"),
]