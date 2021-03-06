from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ratings.models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','contact', 'bio']