from django.contrib import admin

# Register your models here.

from project_two_app.models import User
from .models import NewUser

admin.site.register(User)
admin.site.register(NewUser)
