from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from .services import getInvitations, getInvitation, createInvitation, updateInvitation, deleteInvitation
from django.contrib.auth.decorators import login_required

class InvitationsView(APIView):
    
    # @login_required
    def get(self, request):
        invitations = getInvitations()
        return invitations
    
    # @login_required
    def post(self, request):
        newInvitation = createInvitation(request)
        return newInvitation
    
class InvitationView(APIView):
     
    @login_required
    def get(self, request, invitation_id):
        invitation = getInvitation(request, invitation_id)
        return invitation
    
    @login_required
    def put(self, request, invitation_id):
        updatedInvitation = updateInvitation(request, invitation_id)
        return updatedInvitation
    
    @login_required    
    def delete(self, request, invitation_id):
        deletedInvitation = deleteInvitation(request, invitation_id)
        return deletedInvitation