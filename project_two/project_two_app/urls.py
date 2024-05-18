from django.urls import path

from project_two_app import views

urlpatterns = [
    
    path('user/' , views.records , name = 'record'),
    path('form/' , views.form_name_view , name = 'form_name_view'),
    path('brandnew/' , views.BrandNewFormView , name = 'brandnewformview'),
]
