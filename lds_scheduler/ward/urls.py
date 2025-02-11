from django.urls import path
from .views import WardsView

urlpatterns = [
    path('ward/', WardsView.as_view()),
]