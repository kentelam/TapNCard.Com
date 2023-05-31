from django.http import HttpResponse
from django.shortcuts import render , redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import generic
from .models import Post
import pyqrcode
from io import BytesIO
import os
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class ProfileView(DetailView):

    model = Post

    template_name = 'members/profile.html'

    # Create a function to generate a vcard for a user
    def generate_vcard(self, post):
        first_name = post.full_name.split()[0] if post.full_name else ''
        last_name = post.full_name.split()[1] if len(post.full_name.split()) > 1 else ''
        company = post.business if post.business else ''
        title = post.job_title if post.job_title else ''
        phone_number = post.phone_number if post.phone_number else ''
        address = ''
        email = post.email_address if post.email_address else ''

        vcard = self.make_vcard(first_name, last_name, company, title, phone_number, address, email)
        vcf_file = f'{first_name.lower()}.vcf'
        self.write_vcard(vcf_file, vcard)

        with open(vcf_file, 'rb') as f:
            response = HttpResponse(f.read(), content_type='text/vcard')
            response['Content-Disposition'] = f'attachment; filename="{post.full_name.lower()}.vcf"'

        # Clean up the generated vCard file
        os.remove(vcf_file)

        return response

    def make_vcard(self, first_name, last_name, company, title, phone, address, email):
        address_formatted = ';'.join([p.strip() for p in address.split(',')])
        return [
            'BEGIN:VCARD',
            'VERSION:2.1',
            f'N:{last_name};{first_name}',
            f'FN:{first_name} {last_name}',
            f'ORG:{company}',
            f'TITLE:{title}',
            f'EMAIL;PREF;INTERNET:{email}',
            f'TEL;WORK;VOICE:{phone}',
            f'ADR;WORK;PREF:;;{address_formatted}',
            f'REV:1',
            'END:VCARD'
        ]

    def write_vcard(self, file_path, vcard):
        with open(file_path, 'w') as f:
            f.writelines([l + '\n' for l in vcard])

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        
        if 'download_vcard' in request.GET:
            return self.generate_vcard(context['post'])
        
        return self.render_to_response(context)
    


     # Create a function to generate a QRCode for a user
    def generate_qrcode(self, url):
    # Generate the QR code with a smaller scale
        qr = pyqrcode.create(url)
        scale = 2  # Adjust the scale as desired

        # Create a BytesIO object to hold the image data
        stream = BytesIO()
        qr.png(stream, scale=scale)

        # Return the image response
        response = HttpResponse(content_type='image/png')
        response['Content-Disposition'] = 'inline'
        response.write(stream.getvalue())
        return response

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        
        if 'download_vcard' in request.GET:
            return self.generate_vcard(context['post'])
        
        if 'download_qrcode' in request.GET:
            profile_url = request.build_absolute_uri(self.object.get_absolute_url())
            return self.generate_qrcode(profile_url)

        return self.render_to_response(context)


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
            css_file_path = os.path.join(os.path.dirname(__file__), 'static', 'css', 'profile.css')

            # Open the CSS file and read its contents
            with open(css_file_path, 'r') as css_file:
                css_contents = css_file.read()

            # Replace the current background color with the new one
            new_css_contents = css_contents.replace('background-color: #333333;', f'background-color: {profile.background_color};')

            # Write the updated CSS contents back to the file
            with open(css_file_path, 'w') as css_file:
                css_file.write(new_css_contents)
        

        return redirect('profile', pk=profile.pk)


    return render(request, 'members/edit.html', {'profile': profile, 'background_color':profile.background_color})

