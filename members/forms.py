from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, PostImage
from django.forms import ModelForm
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostImageForm(ModelForm):
    class Meta:
        model = PostImage
        fields = '__all__'