from django.urls import path
from . import views

urlpatterns = [
    path('appoiment/', views.appoiment, name='appoiment' )
]