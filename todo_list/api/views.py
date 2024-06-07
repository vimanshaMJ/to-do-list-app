from dataclasses import fields
from multiprocessing import context
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()
        return context
    

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task  
    context_object_name = 'task'   # for task_detail

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks') 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task' 
    success_url = reverse_lazy('tasks')

class CustomLoginView(LoginView):
    template_name = 'api/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    