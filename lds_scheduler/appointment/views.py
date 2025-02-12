from rest_framework.views import APIView
from .services import get_appointment, get_appointment, create_appointment, update_appointment, delete_appointment


class Appointments(APIView):
    def get(self):
        Appointment = get_appointment()
        return Appointment

    def post(self, request):
        newappointment = create_appointment(request)
        return newappointment
    
class Appointment(APIView):

    def get(self, appointment_id):
        appointment = get_appointment(appointment_id)
        return appointment

    def put(self, request, appointment_id):
        updateappointment = update_appointment(appointment_id, request)
        return updateappointment

    def delete(self, appointment_id):
        appointment = delete_appointment(appointment_id)
        return appointment