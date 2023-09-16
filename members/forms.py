from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile
from django.forms import ModelForm
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class AddProfileForm(ModelForm):

    class Meta:

        model = Post

        fields = ['username','full_name' ,'profile_picture','business','phone_number','email_address','website','job_title','about','background_banner','facebook','instagram','tiktok','twitter','linkedin','paypal','cashapp','snap','discord','twitch','spotify','apple_music','sound_cloud']
	
      

        widgets =  {

            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'business': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'phone_number':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'email_address':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'job_title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'about':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'facebook':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'instagram':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'tiktok':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

           'twitter':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'linkedin':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'paypal':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'cashapp':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'snap':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'discord':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'twitch':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'spotify':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'apple_music':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'sound_cloud':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),


        }


  

class PostForm(ModelForm):

    class Meta:

        model = Post

        fields = ['username','full_name' ,'profile_picture','business','phone_number','email_address','website','job_title','about','background_banner','facebook','instagram','tiktok','twitter','linkedin','paypal','cashapp','snap','discord','twitch','spotify','apple_music','sound_cloud']


        

        widgets =  {

            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'business': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'phone_number':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'email_address':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'job_title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'about':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'facebook':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'instagram':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'tiktok':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

           'twitter':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'linkedin':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'paypal':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'cashapp':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'snap':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'discord':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'twitch':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'spotify':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'apple_music':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

            'sound_cloud':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),


        }





