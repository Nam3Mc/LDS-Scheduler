from django.db import models
from enums.callings import Callings
from ward.models import Ward
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    calling = models.CharField(choices=Callings.choices, default=Callings.MEMBER, max_length=25)
    memberId = models.CharField(max_length=11)
    createAt = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255, default='https://static.vecteezy.com/system/resources/thumbnails/002/318/271/small/user-profile-icon-free-vector.jpg', blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)