from .models import Invitation
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
    