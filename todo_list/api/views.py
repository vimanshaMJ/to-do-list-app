from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'  # for task_list

class TaskDetail(DetailView):
    model = Task  
    context_object_name = 'task'   # for task_detail

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks') 

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task' 
    success_url = reverse_lazy('tasks')

class CustomLoginView(LoginView):
    template_name = 'api/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    