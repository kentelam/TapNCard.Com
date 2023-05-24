from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    username = models.CharField(max_length=50, blank=True, default='@')
   
    card_number = models.CharField(max_length=50, blank=True, default=14)
   
    background_banner = models.ImageField(null=True, blank=True, upload_to='images/profile')
   
    background_color = models.CharField(max_length=20, blank=True, null=True)
    
    profile_picture = models.ImageField(null=True, blank=True, upload_to='images/profile',)
   
    full_name = models.CharField(max_length=100, blank=False)
   
    business = models.CharField(max_length=100, blank=False)
   
    phone_number = models.CharField(max_length=20, blank=True)
   
    email_address = models.EmailField(max_length=100, blank=True)
   
    website = models.URLField(blank=True)
   
    job_title = models.CharField(max_length=100, blank=True)
   
    facebook = models.URLField(blank=True)
   
    instagram = models.URLField(blank=True)
   
    tiktok = models.URLField(blank=True)
   
    twitter = models.URLField(blank=True)
   
    linkedin = models.URLField(blank=True)
   
    paypal = models.URLField(blank=True)
   
    cashapp = models.URLField(blank=True)
   
    snap = models.URLField(blank=True)
   
    discord = models.URLField(blank=True)
   
    twitch = models.URLField(blank=True)
   
    spotify = models.URLField(blank=True)
   
    apple_music = models.URLField(blank=True)
   
    sound_cloud = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}, {self.full_name}, {self.business}, {self.phone_number}, {self.email_address}, {self.website}, {self.job_title}, 's Profile"

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.pk)])
