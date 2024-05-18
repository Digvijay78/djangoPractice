from  django import forms
from project_two_app.models import User
from .models import NewUser



# class FormName(forms.Form):

#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)

class NewUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class BrandNewForm(forms.ModelForm):

    class Meta:
        model = NewUser
        fields = '__all__'