from django.urls import path
from django.http import HttpResponse
from .views import FriendsView, FriendView

urlpatterns = [
    path('', FriendsView.as_view(), name='friends'),
    path('<friend_id>/', FriendView.as_view())
]
