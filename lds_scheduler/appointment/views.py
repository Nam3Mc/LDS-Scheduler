from rest_framework.views import APIView
from .services import get_appointments, get_appointment, create_appointment, update_appointment, delete_appointment

class Appointments(APIView):
    def get(self, request):
        appointments = get_appointments()
        return appointments

    def post(self, request):
        newappointment = create_appointment(request)
        return newappointment

class Appointment(APIView):
    def get(self, request, appointment_id):
        appointment = get_appointment(appointment_id)
        return appointment

    def put(self, request, appointment_id):
        updateappointment = update_appointment(request, appointment_id)
        return updateappointment

    def delete(self, request, appointment_id):
        appointment = delete_appointment(appointment_id)
        return appointment
