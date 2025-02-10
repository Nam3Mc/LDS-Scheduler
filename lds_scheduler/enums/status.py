from django.db import models

class Status(models.TextChoices):
    ACTIVE = 'Active', 'AT'
    COMPLETED = 'Completed', 'CO'
    CANCELED = 'Canceled', 'CA'
    ACEPTED = 'Acepted', 'AC'
    REJECTED = 'Rejected', 'RE'
    EDITED = 'Edited', 'ED'
    INCOMPLETED = 'Incompleted', 'IN'
    PENDING = 'Pending', 'PE'