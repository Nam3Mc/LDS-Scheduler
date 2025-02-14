from .models import Invitation
from appointment.models import Appointment
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializer import InvitationSerializer

def getInvitations():
    invitations = Invitation.objects.all()
    serializer = InvitationSerializer(invitations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def getInvitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, pk=invitation_id)
    serializer = InvitationSerializer(invitation)
    return Response(serializer.data, status=status.HTTP_200_OK)

def createInvitation(request):
    friend_id = request.data.get('friend')
    user_id = request.data.get('user')
    owner_id = request.data.get('owner')
    appointment_id = request.data('appointment')

    if not user_id or not owner_id or appointment_id:
        return Response({'Error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
    
    appointment = Appointment.objects.get(id=appointment)
    if not appointment:
        return Response({'Error': 'Appoiment not found'}, status=status.HTTP_400_BAD_REQUEST)
    
    start_time = appointment.startTime
    end_time = appointment.endTime

    friend_invites = Invitation.objects.filter(friend=friend_id).filter(
        appointment_startTime_lte = end_time,
        appointment_endTime_gte = start_time
    ).count()

    if friend_invites >= 2:
        return Response({'Error', 'Friend already has 2 invotations at the same time'}, status=status.HTTP_400_BAD_REQUEST)
    
    owner_appoiment = Appointment.objects.filter(user=owner_id),filter(
        start_time_lte = end_time,
        end_time_gte = start_time
    )

    if owner_appoiment.exists():
        return Response({'Error', 'Owner has an appointment at the same time'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = InvitationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def updateInvitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, pk=invitation_id)
    serializer = InvitationSerializer(invitation, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def deleteInvitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, pk=invitation_id)
    if invitation:
        invitation.delete()
        return Response( {'message': 'Invitation deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response( {'message': 'Invitation not found'}, status=status.HTTP_404_NOT)
    