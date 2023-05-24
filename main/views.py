from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import ContactForm, PostForm
import os

# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})



class HomeView(ListView):

    model = Post

    template_name = 'home.html'



class ProfileView(DetailView):

    model = Post

    template_name = 'profile.html'





#@login_required
def profile_editor(request, pk):

    
    # Get the UserProfile object for the given pk, or create a new one.
    profile = get_object_or_404(Post, pk=pk) if pk else Post()


    if request.method == "POST":

        # Update the profile with the POST data.
        profile.background_banner = request.FILES.get('background_banner')
        
        profile.background_color = request.POST.get('background_color')        
        
        profile.profile_picture = request.FILES.get('profile_picture')
        
        profile.full_name = request.POST.get("full_name")
        
        profile.business = request.POST.get("business")
        
        profile.phone_number = request.POST.get("phone_number")
        
        profile.email_address = request.POST.get("email_address")
        
        profile.website = request.POST.get("website")
        
        profile.job_title = request.POST.get("job_title")
        
        profile.facebook = request.POST.get("facebook")
        
        profile.instagram = request.POST.get("instagram")
        
        profile.tiktok = request.POST.get("tiktok")
        
        profile.twitter = request.POST.get("twitter")
        
        profile.linkedin = request.POST.get("linkedin")
        
        profile.paypal = request.POST.get("paypal")
        
        profile.cashapp = request.POST.get("cashapp")
        
        profile.snap = request.POST.get("snap")
        
        profile.discord = request.POST.get("discord")
        
        profile.twitch = request.POST.get("twitch")
        
        profile.spotify = request.POST.get("spotify")
        
        profile.apple_music = request.POST.get("apple_music")
        
        profile.sound_cloud = request.POST.get("sound_cloud")

        profile.save()
        
        # Check if a new background color was submitted
      
        if profile.background_color:

            # Get the path to the CSS file
            css_file_path = os.path.join(os.path.dirname(__file__), 'static', 'css', 'style.css')

            # Open the CSS file and read its contents
            with open(css_file_path, 'r') as css_file:
                css_contents = css_file.read()

            # Replace the current background color with the new one
            new_css_contents = css_contents.replace('background-color: #333333;', f'background-color: {profile.background_color};')

            # Write the updated CSS contents back to the file
            with open(css_file_path, 'w') as css_file:
                css_file.write(new_css_contents)
        

        return redirect('profile', pk=profile.pk)


    return render(request, 'edit.html', {'profile': profile, 'background_color':profile.background_color})




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