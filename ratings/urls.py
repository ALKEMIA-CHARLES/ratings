from django.conf.urls import url
from .views import ProjectListView
urlpatterns = [
    url(r'^$', ProjectListView.as_view(), name='index')
]