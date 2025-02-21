from .models import User
from django.shortcuts import get_object_or_404
from .serializer import UserSerializer, LoginSerializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

def getUsers():
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return serializer.data

def getUser(user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user)
    return serializer.data

def singUp(request):
    user_number_id = request.data.get('memberId')

    if User.objects.filter(memberId=user_number_id).exists():
        return {'error': 'This user already exists'}, 400  # Se devuelve un diccionario y código de error

    request.data['password'] = make_password(request.data.get('password'))
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return serializer.data, 201
    return serializer.errors, 400

def updateUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return serializer.data, 200
    return serializer.errors, 400

def deleteUser(user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return {'message': 'User deleted successfully'}, 204

def sing_In(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(email=email)
            userData = get_object_or_404(User, pk=email)

            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return {"refresh": str(refresh), "access": str(refresh.access_token), 'user': User(userData)}, 200
            else:
                return {"error": "Invalid Credentials"}, 401
        except User.DoesNotExist:
            return {"error": "Invalid Credentials"}, 401

    return serializer.errors, 400