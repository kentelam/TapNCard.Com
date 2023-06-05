from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from main .forms import  PostForm
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')