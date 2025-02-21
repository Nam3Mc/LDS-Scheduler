from django.urls import path
from .views import FriendsView, FriendView

urlpatterns = [
    path('friends/', FriendsView.as_view(), name='friends'),
    path('friend/<friend_id>/', FriendView.as_view())
]
