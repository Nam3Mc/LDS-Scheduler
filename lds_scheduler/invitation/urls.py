from django.urls import path
from .views import Invitations, Invitation

urlpatterns = [
    path('invitations/', Invitations.as_view(), name='invitation' ),
    path('invitation/<uuid:invitation_id>/', Invitation.as_view(), name='invitation' )
]