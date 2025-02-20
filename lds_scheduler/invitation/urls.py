from django.urls import path
from .views import InvitationsView, InvitationView

urlpatterns = [
    path('', InvitationsView.as_view(), name='invitations' ),
    path('<uuid:invitation_id>/', InvitationView.as_view(), name='invitation' )
]