from rest_framework.response import Response
from rest_framework import status
from .models import Friend
from .serializer import FriendSerializer
from django.shortcuts import get_object_or_404

def  getFriends():
    friends = Friend.objects.all()
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def getFriend(request, friend_id):
    friend = get_object_or_404(Friend, pk=friend_id)
    serializer = FriendSerializer(friend)
    return Response(serializer.data, status=status.HTTP_200_OK)

def createFriend(request):
    serializer = FriendSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def updateFriend(request, friend_id):
    friend = get_object_or_404(Friend, pk=friend_id)
    serializer = FriendSerializer(friend, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def deleteFriend(request, friend_id):
    friend = get_object_or_404(Friend, pk=friend_id)
    if friend:
        friend.delete()
        return Response( {'message': 'Friend deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response( {'message': 'Friend not found'}, status=status.HTTP_404_NOT_FOUND)

