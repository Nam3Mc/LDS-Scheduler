from django.db import models
from users.models import User
from friend.models import Friend
import uuid

class Ward(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255)
    unitId = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)