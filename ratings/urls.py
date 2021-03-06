from django.conf.urls import url
from .views import ProjectListView, ProjectDetailView, ProjectCreateView
from . import views

urlpatterns = [
    url(r'^$', ProjectListView.as_view(), name='index'),
    url(r'^project/(?P<pk>\d+)/$', ProjectDetailView.as_view(), name='project-detail'),
    url(r'^project/new/$', ProjectCreateView.as_view(), name='project-create'),
    url(r'^search/$', views.search, name="search"),
]