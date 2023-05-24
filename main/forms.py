from django import forms
from django.forms import ModelForm
from . models import Post

class ContactForm(forms.Form):
    
        name = forms.CharField()
        message = forms.ChoiceField(widget=forms.Textarea)



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
