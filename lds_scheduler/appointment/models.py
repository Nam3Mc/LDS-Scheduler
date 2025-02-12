from django.db import models
from users.models import User
from enums.status import Status
from enums.types import Type
import uuid

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    startTime = models.TimeField(null=False)
    endTime = models.TimeField(null=False) 
    description = models.TextField()
    status = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=20)
    type = models.CharField(choices=Type.choices, default=Type.TEACHING, max_length=20)
    user = models.ManyToManyField(User)