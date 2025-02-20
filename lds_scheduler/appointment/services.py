from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from .serializer import AppointmentSerializer
from django.shortcuts import get_object_or_404

def get_appointments():
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def get_appointment(appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data, status=status.HTTP_200_OK)

def create_appointment(request):
    start = request.data.get('startTime')
    end = request.data.get('endTime')
    user = request.data.get('user')
    friend = request.data.get('friend')

    if not start or not end or not user:
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    if Appointment.objects.filter(user=user, startTime__lte=end, endTime__gte=start).exists():
        return Response({'error': 'User already has an appointment in this time range'}, status=status.HTTP_400_BAD_REQUEST)

    if friend and Appointment.objects.filter(friend=friend, startTime__lte=end, endTime__gte=start).exists():
        return Response({'error': 'Friend already has an appointment in this time range'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_appointment(appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    return Response({'message': 'Appointment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
