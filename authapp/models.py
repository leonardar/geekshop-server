from datetime import timedelta
from django.utils.timezone import now

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    is_deleted = models.BooleanField(default=False)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expire = models.DateTimeField(default=(now()+timedelta(hours=48)))

    def activation_key_is_expired(self):
        if now() <= self.activation_key_expire:
            return False
        return True


