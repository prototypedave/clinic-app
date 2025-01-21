from django.urls import path
from . import views

urlpatterns = [
    path("add-appointment", views.AddAppointmentsView.as_view(), name='add-appointment'),
    path("get-appointments", views.RetrieveAppointmentView.as_view(), name='get-appointments'),
    path("update-appointments", views.UpdateAppointmentDatesView.as_view(), name='update-appointments'),
]