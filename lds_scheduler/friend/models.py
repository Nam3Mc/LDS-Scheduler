from django.db import models
import uuid
from ward.models import Ward

class Friend(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    lessons = models.IntegerField(blank=True, null=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)