from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from members.models import Post
from .models import Tapncard
from .forms import ContactForm
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

        tapncard = Tapncard.objects.first()  # Get the first Tapncard object (you can modify this logic as needed)

        context['tapncard'] = tapncard

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
    
    
    tapncard = Tapncard.objects.first()  # Get the first Tapncard object (y>
   
      
    return render(request, 'main/about.html', {'tapncard': tapncard})




class ContactFormView(FormView):

    form_class = ContactForm

    template_name = 'main/contact.html'

    # URL NOT a template.html
    success_url = '/thankyou/'
    
    # Tapncard.com Logo
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     tapncard = Tapncard.objects.first()  # Get the first Tapncard object (you can modify this logic as needed)
     context['tapncard'] = tapncard
     return context

    # what to do with form?
    def form_valid(self, form):

       print(form.cleaned_data)
       #email
    
       return super().form_valid(form)
   
 



class ThankYouView(TemplateView):
    template_name = 'main/thankyou.html'
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     tapncard = Tapncard.objects.first()  # Get the first Tapncard object (you can modify this logic as needed)
     context['tapncard'] = tapncard
     return context



class PrivacyView(TemplateView):
    template_name = 'main/privacy.html'
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     tapncard = Tapncard.objects.first()  # Get the first Tapncard object (you can modify this logic as needed)
     context['tapncard'] = tapncard
     return context



    
class TermsView(TemplateView):
    template_name = 'main/terms.html'
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     tapncard = Tapncard.objects.first()  # Get the first Tapncard object (you can modify this logic as needed)
     context['tapncard'] = tapncard
     return context




