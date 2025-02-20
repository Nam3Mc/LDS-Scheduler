from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from .services import getUsers, getUser, createUser, updateUser, deleteUser
from django.contrib.auth.decorators import login_required

class Users(APIView):
    
        def get(self, request):
            users = getUsers()
            return users
    
        def post(self, request):
            newUser = createUser(request)
            return newUser

class User(APIView):
     
        # @login_required
        def get(self, request, user_id):
            user = getUser( user_id)
            return user
        
        # @login_required
        def put(self, request, user_id):
            updatedUser = updateUser(request, user_id)
            return updatedUser
        
        # @login_required
        def delete(self, request, user_id):
            deletedUser = deleteUser(request, user_id)
            return deletedUser