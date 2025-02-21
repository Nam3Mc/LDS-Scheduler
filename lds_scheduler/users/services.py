from .models import User
from django.shortcuts import get_object_or_404
from .serializer import UserSerializer, LoginSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status  # 🔹 Importación corregida
import time

def getUsers():
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return serializer.data

def getUser(user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user)
    return serializer.data

def sign_up(request):
    user_number_id = request.data.get('memberId')

    if User.objects.filter(memberId=user_number_id).exists():
        return Response({'error': 'This user already exists'}, status=status.HTTP_400_BAD_REQUEST)  # 🔹 Corregido con Response

    request.data['password'] = make_password(request.data.get('password'))
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # 🔹 Se devuelve una Response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 🔹 Corregido

def updateUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteUser(user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

def sign_in(request):
    serializer = LoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 🔹 Corrección

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    try:
        user = User.objects.get(email=email)

        if not check_password(password, user.password):
            time.sleep(2)  # 🔹 Pequeño retraso para evitar ataques de fuerza bruta
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        userData = {
            "name": user.name,
            "lastName": user.lastname,
            "memberId": user.memberId,
            "address": user.address,
            "calling": user.calling,
            "ward": user.ward.name if user.ward else None,
            "id": user.pk,
        }

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "userData": userData
        }, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        time.sleep(2)  # 🔹 Retraso para evitar ataques de enumeración de usuarios
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
