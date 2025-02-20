from rest_framework.response import Response
from rest_framework import status
from .models import Friend
from .serializer import FriendSerializer
from django.shortcuts import get_object_or_404

def getFriends():
    friends = Friend.objects.all()
    serializer = FriendSerializer(friends, many=True)
    return serializer.data  # Devuelve solo los datos, no un Response

def getFriend(friend_id):
    friend = get_object_or_404(Friend, pk=friend_id)
    serializer = FriendSerializer(friend)
    return serializer.data  # Devuelve solo los datos

def createFriend(request):
    serializer = FriendSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def updateFriend(request, friend_id):
    friend = get_object_or_404(Friend, pk=friend_id)
    serializer = FriendSerializer(friend, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def deleteFriend(friend_id):
    friend = get_object_or_404(Friend, pk=friend_id)
    friend.delete()
    return Response({'message': 'Friend deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
