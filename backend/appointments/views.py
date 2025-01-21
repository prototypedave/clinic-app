from rest_framework.views import APIView
from .serializers import AppointmentsSerializer, RescheduleSerializer
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from .models import Appointments

class AddAppointmentsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        appointment = AppointmentsSerializer(data=request.data)
        if appointment.is_valid():
            appointment.save()
            return JsonResponse({"message": "Appointment saved successfully"}, status=201)
        return JsonResponse({"error": "Error saving appointment"}, status=400)
    

class RetrieveAppointmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        appointments = Appointments.get_upcoming_appointments()
        return JsonResponse({"events": appointments}, status=200)
    

class UpdateAppointmentDatesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        appoint_id = request.data.get('id')
        appointment = Appointments.get(pk=appoint_id)
        field = {
            "start": request.data.get('start'),
            "end": request.data.get('end'),
            "reschedule_reason": request.data.get('reason')
        }
        event_update = RescheduleSerializer(appointment, field, partial=True)
        if event_update.is_valid():
            event_update.save()
            return JsonResponse({"message": "Appointment rescheduled successfully"}, status=201)
        return JsonResponse({"error": "Failed to reschedule appointment"}, status=400)