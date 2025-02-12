from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import getFriends, getFriend, createFriend, updateFriend, deleteFriend

class Friends(APIView):
    def get(self, request):
        friends = getFriends()
        return Response(friends)

    def post(self, request):
        newFriend = createFriend(request)
        return Response(newFriend, status=status.HTTP_201_CREATED)

class Friend(APIView):
    
    def get(self, request, friend_id):
        friend = getFriend(request, friend_id)
        return Response(friend)
    
    def put(self, request, friend_id):
        updatedFriend = updateFriend(request, friend_id)
        return Response(updatedFriend)
    
    def delete(self, request, friend_id):
        deletedFriend = deleteFriend(request, friend_id)
        return Response(deletedFriend)