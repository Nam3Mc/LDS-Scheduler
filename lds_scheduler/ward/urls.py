from django.urls import path
from . import views

urlpatterns = [
    path('ward/', views.ward, name='ward' ),
    path('ward/add/', views.add, name='add')
]