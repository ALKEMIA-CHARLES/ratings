from django.db import models
from pyuploadcare.dj.models import ImageField
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("=========================================[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]=")

    if created:
        Profile.objects.create(user=instance)
        print("==========================================")


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='pictures')
    contact = models.EmailField(max_length=250)

    def __str__(self):
        return f'{self.user.username} Profile'



class Project(models.Model):
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

class Repositories(models.Model):
    title = models.EmailField(max_length=250)
    image = models.ImageField(default="deafult.jpg", upload_to='pictures')
    description = models.TextField(max_length=300)
    link = models.URLField(max_length=250)