from django.urls import path
from basic_app import views


#template tags
app_name = 'basic_app'

urlpatterns = [
     path( 'register/' , views.register , name = 'register' ),
     path( 'login/' , views.user_login , name = 'login' ),
]
