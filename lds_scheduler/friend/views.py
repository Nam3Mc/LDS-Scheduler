from rest_framework.views import APIView
from rest_framework.response import Response
from .services import getFriends, getFriend, createFriend, updateFriend, deleteFriend

class FriendsView(APIView):
   
    def get(self, request):
        return getFriends()

    def post(self, request):
        return createFriend(request)  

class FriendView(APIView):
    
    def get(self, request, friend_id):
        return getFriend(friend_id) 

    def put(self, request, friend_id):
        return updateFriend(friend_id, request)
    
    def delete(self, request, friend_id):
        return deleteFriend(friend_id) 
