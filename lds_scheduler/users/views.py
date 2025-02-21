from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import getUsers, getUser, singUp, updateUser, deleteUser, sing_In

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
    
class SingIn(APIView):

    def post(self, request):
        user, status_code = sing_In(request)
        return Response(user, status=status_code)

class SingUp(APIView):
       
    def post(self, request):
        user = singUp(request)
        return Response(user, tatus=status.HTTP_201_CREATED)