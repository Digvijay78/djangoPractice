from django.db import models
from django.urls import reverse


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=256, unique=True)
    principal = models.CharField(max_length=100, default='Default Principal Name')
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={"pk": self.pk})
    


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveBigIntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE , related_name='students')

    def __str__(self):
        return self.name
