from django.db import models
from users.models import User
from friend.models import Friend
from appointment.models import Appointment
from enums.status import Status
import uuid

class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True , editable=False)
    owner = models.ManyToManyField(User, related_name='invitation_owner')
    status = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=20)
    user = models.ManyToManyField(User, related_name='invited')
    friend = models.ManyToManyField(Friend)
    appointment = models.ManyToManyField(Appointment)
