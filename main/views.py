from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from members.models import Post
from .forms import ContactForm, PostForm
import nfc
import pyqrcode
from io import BytesIO
import os

# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})



class HomeView(ListView):

    model = Post

    template_name = 'main/home.html'

    context_object_name = 'posts'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve the post object based on your logic
        post = Post.objects.first()  # Replace this with your actual logic
        
        context['post'] = post
        return context


def search_view(request):

    if request.method == 'POST':

        searched = request.POST['searched']

        profile = Post.objects.filter(username__contains=searched )


        return render(request, 'main/search.html', {

            'searched': searched,
            'profile':profile,
        })
    
    else:
        return render(request, 'main/search.html')




def about(request):
    return render(request, 'main/about.html', {})




class ContactFormView(FormView):

    form_class = ContactForm

    template_name = 'main/contact.html'

    # URL NOT a template.html
    success_url = '/thankyou/'

    # what to do with form?
    def form_valid(self, form):

        print(form.cleaned_data)
    
        return super().form_valid(form)
    



class ThankYouView(TemplateView):
    template_name = 'main/thankyou.html'