from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    phone = models.BigIntegerField(max_length=15)
    lessons = models.IntegerField(max_length=999)
