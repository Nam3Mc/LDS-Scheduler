from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import getUsers, getUser, sign_up, updateUser, deleteUser, sign_in

class Users(APIView):

    def get(self, request):
        users = getUsers()  
        return Response(users, status=status.HTTP_200_OK)

class User(APIView):
    # permission_classes = [IsAuthenticated]  

    def get(self, request, user_id):
        user = getUser(user_id)
        return Response(user, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        updated_user = updateUser(request, user_id)
        return Response(updated_user, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        deleteUser(request, user_id)
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class SignIn(APIView):

    def post(self, request):
        return sign_in(request)  # Ya devuelve una Response

class SignUp(APIView):
       
    def post(self, request):
        return sign_up(request)  # Ya devuelve una Response
