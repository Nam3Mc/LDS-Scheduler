from django.db import models
import uuid
class Friend(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    lessons = models.IntegerField()
