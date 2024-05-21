from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Login(models.Model):
    
    name = models.CharField(max_length=264 , unique=True)
    email = models.EmailField(max_length=264, unique= True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)