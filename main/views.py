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

    template_name = 'home.html'




class ContactFormView(FormView):

    form_class = ContactForm

    template_name = 'contact.html'

    # URL NOT a template.html
    success_url = 'thankyou.html'

    # what to do with form?
    def form_valid(self, form):

        print(form.cleaned_data)

        form.save(form.cleaned_data)

        return super().form_valid(form)
    



class ThankYouView(TemplateView):
    template_name = 'thankyou.html'