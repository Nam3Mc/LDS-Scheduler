from .models import User
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializer import UserSerializer

def getUsers():
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def getUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

def createUser(request):
    user_number_id = request.data.get('memberId')
    user = User.objects.filter(memberId='user_number_id')

    if user:
        return Response({'Error', 'This user already exist'})
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def updateUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def deleteUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user:
        user.delete()
        return Response( {'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response( {'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)