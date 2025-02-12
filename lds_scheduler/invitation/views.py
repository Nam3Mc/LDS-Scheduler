from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from .services import getInvitations, getInvitation, createInvitation, updateInvitation, deleteInvitation

class Invitations(APIView):
    
    def get(self, request):
        invitations = getInvitations()
        return invitations
    
    def post(self, request):
        newInvitation = createInvitation(request)
        return newInvitation
    
class Invitation(APIView):
     
    def get(self, request, invitation_id):
        invitation = getInvitation(request, invitation_id)
        return invitation
        
    def put(self, request, invitation_id):
        updatedInvitation = updateInvitation(request, invitation_id)
        return updatedInvitation
        
    def delete(self, request, invitation_id):
        deletedInvitation = deleteInvitation(request, invitation_id)
        return deletedInvitation