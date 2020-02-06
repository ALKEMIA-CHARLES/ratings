from django.db import models
from pyuploadcare.dj.models import ImageField
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(default="default.jpg", upload_to='pictures' )
    description = models.TextField(max_length=250)
    link =  models.URLField(max_length=250)
    post_date = models.DateTimeField(auto_now_add=True)


    @classmethod
    def show_projects(cls):
        return cls.objects.order("post_date")[::1]
    @classmethod
    def search_projects_by_title(cls,search):
        return cls.objects.filter(name__icontains=search)
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='pictures')
    contact = models.EmailField(max_length=250)

class repositories(models.Model):
    title = models.EmailField(max_length=250)
    image = models.ImageField(default="deafult.jpg", upload_to='pictures')
    description = models.TextField(max_length=300)
    link = models.URLField(max_length=250)