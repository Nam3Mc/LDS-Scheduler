from django.urls import path
from .views import Users, User

urlpatterns = [
    path('', Users.as_view(), name='users' ),
    path('<uuid:user_id>/', User.as_view(), name='user' )
]