from django.urls import path
from .views import InvitationsView, InvitationView

urlpatterns = [
    path('invitations/', InvitationsView.as_view(), name='invitations' ),
    path('invitation/<uuid:invitation_id>/', InvitationView.as_view(), name='invitation' )
]