from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from ratings.models import Profile, Project, Repositories
# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = "main/index.html"
    context_object_name = "projects"
    ordering = ['-post_date']


def register(request):
    form = UserCreationForm()
    return render(request, 'main/register.html', {'form':form})
# def register(request):
#     projects = Project.show_projects()
#     return render(request, 'main/index.html', context={"projects":projects})