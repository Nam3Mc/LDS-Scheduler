from django.db import models
import uuid

class Ward(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)
    unitId = models.BigIntegerField()