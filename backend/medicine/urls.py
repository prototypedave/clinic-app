from django.urls import path
from . import views

urlpatterns = [
    path("add-medicine", views.AddMedicineView.as_view(), name='add-medicine'),
    path("get-expired", views.NotifyExpiry.as_view(), name="medicine-expiry"),
]