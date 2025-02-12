from django.db import models
from users.models import User
from friend.models import Friend
# from appointment.models import appointment
from enums.status import Status
import uuid

class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True , editable=False)
    status = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=20)
    user = models.ManyToManyField(User)
    friend = models.ManyToManyField(Friend)
    # appointment = models.ManyToManyField(appointment)
