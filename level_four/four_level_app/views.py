from django.shortcuts import render
from .forms import UserForm
from .models import Login

# Create your views here.

def index(request):

    context_dict = {
        'name' : "welcome to the index page",
        'number1' : 100,
        'number2' : 70,
    }

    return render(request, 'level_four_app/index.html' , context= context_dict )


def login(request):

    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
        else :
            print('error')

    return render (request , 'level_four_app/login.html' , {'form' : form})        


def user (request):

    user_details = Login.objects.order_by('name')

    user_access = {
        'user_info' : user_details
    }

    return render (request , 'level_four_app/user.html' , context=user_access)