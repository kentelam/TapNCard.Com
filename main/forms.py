from django import forms
from django.forms import ModelForm
from  members.models import Post

class ContactForm(forms.Form):
    
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
