from django.urls import path
from .views import WardsView, WardById

urlpatterns = [
    path('', WardsView.as_view(), name='wards'),
    path('<uuid:ward_id>/', WardById.as_view(), name='ward'),
]