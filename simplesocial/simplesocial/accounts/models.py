from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.

class User(AbstractUser, PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
