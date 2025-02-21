from django.urls import path
from .views import Users, User, SignIn, SignUp

urlpatterns = [
    path('users/', Users.as_view(), name='users-list'),
    path('user/<uuid:user_id>/', User.as_view(), name='user-detail'),
    path('signin/', SignIn.as_view(), name='sign-in'),
    path('signup/', SignUp.as_view(), name='sign-up'),
]
