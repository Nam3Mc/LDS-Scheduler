from django.urls import path
from .views import Appointments, Appointment

urlpatterns = [
    path('appointments/', Appointments.as_view() ),
    path('appointment/<uuid:appointment_id>/', Appointment.as_view() ),
]