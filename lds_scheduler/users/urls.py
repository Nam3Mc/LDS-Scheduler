from django.urls import path
from .views import Users, User, SingIn, SingUp

urlpatterns = [
    path('users/', Users.as_view() ),
    path('user/<uuid:user_id>/', User.as_view() ),
    path('signin/', SingIn.as_view() ),
    path('signup/', SingUp.as_view() )
]