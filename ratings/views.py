from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from ratings.models import Profile, Project, Repositories
from django.contrib import messages
# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = "main/index.html"
    context_object_name = "projects"
    ordering = ['-post_date']


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', context={'form':form})