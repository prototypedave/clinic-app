from django.urls import path
from . import views

urlpatterns = [
    path("add-expense", views.AddExpenseView.as_view(), name='add-expense'),
]