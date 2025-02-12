from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from .services import getUsers, getUser, createUser, updateUser, deleteUser

class Users(APIView):
    
        def get(self, request):
            users = getUsers()
            return users
    
        def post(self, request):
            newUser = createUser(request)
            return newUser

class User(APIView):
     
        def get(self, request, ward_id):
            user = getUser(request, ward_id)
            return user
        
        def put(self, request, ward_id):
            updatedUser = updateUser(request, ward_id)
            return updatedUser
        
        def delete(self, request, ward_id):
            deletedUser = deleteUser(request, ward_id)
            return deletedUser