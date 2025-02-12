from django.urls import path
from .views import Friend, Friends

urlpatterns = [
    path('friends/', Friends.as_view(), name='friends' ),
    path('friend/<uuid:friend_id>/', Friend.as_view(), name='friend' )
]