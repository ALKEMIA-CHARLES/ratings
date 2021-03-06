from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from ratings.models import Profile, Project, Repositories
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from ratings.forms import UserUpdateForm
# Create your views here.


class ProjectListView(LoginRequiredMixin,ListView):
    model = Project
    template_name = "main/index.html"
    context_object_name = "projects"
    ordering = ['-post_date']

class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = "main/detail.html"

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = "main/projectform.html"
    fields = ['title', 'image', 'description']

    def form_valid(self, form):
        form.instance.masterkey = self.request.user
        return super().form_valid(form)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you are now able to login')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', context={'form':form})

@login_required
def search(request):
    if request.method == "GET":
        search_term = request.GET.get("search")
        searched_post = Project.search_projects_by_title(search_term)
        results = len(searched_post)
        message = "{}".format(search_term)
        
        return render(request, "main/search.html", context={"message":message,
                                                            "projects":searched_post,
                                                            "results":results})
    else:
        message = "You have not searched for any user"
        return render(request, "main/index.html", context={"message":message})

@login_required
def profile(request):
    repos = Repositories.objects.all()[::1]
    if request.method == "POST":
        form = UserUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user.profile)
    return render(request, "main/profile.html", context={"form":form,
                                                           "repos":repos 
                                                      })
