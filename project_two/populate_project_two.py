import os

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings')

import django
django.setup()

import random
from project_two_app.models import User 

from faker import Faker

fake = Faker()


def populate(N=5):
    name_model =[]  
    for entry in range(N):

     fake_name = fake.name()
     fake_last = fake.company()
     fake_email = fake.email()

     name_model,created = User.objects.get_or_create(first_name = fake_name , last_name = fake_last, email = fake_email)[0]
     if created:
      name_model.save()  

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating Successfull")