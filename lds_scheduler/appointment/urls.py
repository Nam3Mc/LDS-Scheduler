from django.urls import path
from .views import Appointments, Appointment

urlpatterns = [
    path('', Appointments.as_view() ),
    path('<uuid:appointment_id>/', Appointment.as_view() ),
]