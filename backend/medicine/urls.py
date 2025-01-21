from django.urls import path
from . import views

urlpatterns = [
    path("add-medicine", views.AddMedicineView.as_view(), name='add-medicine'),
]