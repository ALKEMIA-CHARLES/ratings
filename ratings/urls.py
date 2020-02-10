from django.conf.urls import url
from .views import ProjectListView, ProjectDetailView
urlpatterns = [
    url(r'^$', ProjectListView.as_view(), name='index'),
    url(r'^project/(?P<pk>\d+)/$', ProjectDetailView.as_view(), name='project-detail')
]