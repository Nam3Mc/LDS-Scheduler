from django.urls import path
from .views import WardsView, WardById

urlpatterns = [
    path('wards/', WardsView.as_view(), name='wards'),
    path('ward/<uuid:ward_id>/', WardById.as_view(), name='ward'),
]