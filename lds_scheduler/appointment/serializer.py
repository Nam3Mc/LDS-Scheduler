from rest_framework.serializers import ModelSerializer
from .models import Appointment

class Appointmenterializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'