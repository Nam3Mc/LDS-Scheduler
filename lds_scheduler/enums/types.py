from django.db import models

class Type(models.TextChoices):
    FAMILYHOMEEVENING = 'FamilyHomeEvening', 'FHV'
    SERVICE = 'Service', 'SE'
    MINISTERING = 'Ministering', 'MI'
    TEACHING = 'Teaching', 'TA'