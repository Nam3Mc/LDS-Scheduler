from django.urls import path
from .views import Users, User

urlpatterns = [
    path('users/', Users.as_view(), name='users' ),
    path('users/<uuid:user_id>/', User.as_view(), name='user' )
]