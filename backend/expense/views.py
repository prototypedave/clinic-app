from rest_framework.views import APIView
from .serializers import ExpenseSerializer
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from .models import Expense


class AddExpenseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        expense_data = request.data.copy()
        expense_data['reported_by'] = user.id

        expense = ExpenseSerializer(data=expense_data)
        if expense.is_valid():
            expense.save()
            return JsonResponse({"message": "Expense Updated Successfully"}, status=201)
        return JsonResponse({"error": "Error updating expense.Please try again"}, status=400)