from django.urls import path
from . import views


app_name = 'basicapp'

urlpatterns = [
    path('' , views.index , name = 'index' ),
    path('login/' , views.login , name ='login'),
    path('user/' , views.user , name ='user'),
]