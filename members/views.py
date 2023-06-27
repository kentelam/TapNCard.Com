from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render , redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from .models import Post, Profile
from main .models import Tapncard
from .forms import PostForm, AddProfileForm
import pyqrcode
from io import BytesIO
import os

# Create your views here.


def change_password(request):
    tapncard = Tapncard.objects.first()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error('Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form, 'tapncard': tapncard})






class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
   
    success_url = reverse_lazy('login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tapncard = Tapncard.objects.first()  # Get the first Tapncard object (y>
        context['tapncard'] = tapncard
        return context


class AddProfileView(CreateView):

    model = Post

    
    form_class = AddProfileForm

    template_name = 'registration/add-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tapncard = Tapncard.objects.first()  # Get the first Tapncard object (y>
        context['tapncard'] = tapncard
        return context


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class ProfileView(DetailView):

    model = Post
   
    
    template_name = 'members/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tapncard = Tapncard.objects.first()  # Get the first Tapncard object (y>
        context['tapncard'] = tapncard
        return context


    # Search Function to Query Post model in multiple fields
    def get_queryset(self):

        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(username__icontains=search_query) |
                Q(company__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(website__icontains=search_query) |
                Q(title__icontains=search_query)
            )
        return queryset


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


    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            tapncard = Tapncard.objects.first()  # Get the first Tapncard object (y>
            context['tapncard'] = tapncard
            return context




def profile_editor(request, pk):

   
    tapncard = Tapncard.objects.first()  # Get the first Tapncard object (y>
       

    # Get the UserProfile object for the given pk, or create a new one.
    post = get_object_or_404(Post, pk=pk) if pk else Post()

    form = PostForm(request.POST or None, instance=post)
    
    # Get the associated Post object

    if request.method == "POST":
        # Update the profile with the POST data.
        
        form = PostForm(request.POST, request.FILES or None, instance=post)

        if form.is_valid():

            # Save both the profile and post image
            form.save()
        
            return redirect('profile', pk=post.pk)

    return render(request, 'members/edit.html', {'post': post, 'form':form, 'tapncard':tapncard})





def pet_profile(request):
        tapncard = Tapncard.objects.first()  # Get the first Tapncard object (y>

        return render(request, 'members/petprofile.html', {
            'tapncard':tapncard,
            #'searched': searched,
            #'profile':profile,
        })
