from django.shortcuts import render
from project_two_app.models import User
# from project_two_app.form import FormName
# from .forms import FormName 
from .form import NewUserForm
from .form import BrandNewForm

# Create your views here.

def index(request):
    my_dict = {
        'insert_me' : 'Hello i m from views',
        'insert_you' : "hey there i am using django"
    }   
    return render (request, 'project_two_app/index.html', context = my_dict)

def records(request):

    # records = User.objects.order_by('email')

    # records_data  = {
    #     'records_name' : records
    # }

    # return render(request, 'project_two_app/records.html', context=records_data)
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('Error form invalid')

    return render(request, 'project_two_app/records.html', {'form':form})        



def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():

            print("Form Validation Success")
            print("Name:" + form.cleaned_data['name'])
            print("Email:" + form.cleaned_data['email'])
            print("Text:" + form.cleaned_data['text'])


    return render(request, 'project_two_app/form_name.html', {'form':form} )



def BrandNewFormView(request):

    form = BrandNewForm()

    if request.method == 'POST':

        form = BrandNewForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        
        else :
            print('Error form invalid')


    return render(request , 'project_two_app/brandnew.html', {'form' : form } )        

