from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy 
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView , ListView,DetailView , UpdateView , DeleteView
from .models import Student,School

# Create your views here.

# def index(request):

#     return render(request , 'basic_app/index.html')

# class CBView(View):

#     def get(self,request):
#         return HttpResponse("Class Based Views")

class IndexView(TemplateView):
    template_name = "basic_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "basic Injection"
        return context
    

# class Admission(CreateView):

#     template_name = "baisc_app/admission.html"
#     form = School()
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = form
        

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School
    template_name = 'basic_app/school_list.html'


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name='basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ['name', 'principal', 'location']
    model = School
    template_name='basic_app/school_form.html'

   
class SchoolUpdateView(UpdateView):
    fields = ['name', 'principal']
    model = School
    #it automatically connect itself with something school_form.html


class SchoolDeleteView(DeleteView):
    context_object_name = 'school'
    model = School
    success_url = reverse_lazy('basic_app:list')
    template_name = 'basic_app/school_confirm_delete.html'


class StudentUpateView(UpdateView):
    fields = ['name', 'age', 'school']
    model = Student


class StudentDeleteView(DeleteView):
    context_object_name = 'student'
    model = Student
    # success_url = reverse_lazy('basic_app:detail', pk = Student.pk )
    template_name = 'basic_app/student_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('basic_app:detail', kwargs={'pk': self.object.school.pk})