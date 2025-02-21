from django.db import models
from enums.callings import Callings
from ward.models import Ward
import uuid
from django.contrib.auth.hashers import make_password, check_password

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

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):  
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        """Hashea la contraseña correctamente."""
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)