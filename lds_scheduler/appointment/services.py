from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from .serializer import Appointmenterializer
from django.shortcuts import get_object_or_404

def get_appointment():
    appointment = Appointment.objects.all()
    serializer = Appointmenterializer(appointment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def get_appointment(appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    serializer = Appointmenterializer(appointment)
    return Response(serializer.data, status=status.HTTP_200_OK)

def create_appointment(request):
    start = request.data.get('startTime')
    end = request.data.get('endTime')
    user = request.data.get('user')
    friend = request.data.get('friend')

    if not start or not user:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if Appointment.objects.filter(user=user).filter(
        startTime__lte=end, 
        endTime__gte=start
    ).exists():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if friend and Appointment.objects.filter(friend=friend).filter(
        startTime__lte=end, 
        endTime__gte=start
    ).exists():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    serializer = Appointmenterializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def update_appointment(appointment_id, request):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    serializer = Appointmenterializer(appointment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_appointment(appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if appointment:
        Appointment.delete()
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)