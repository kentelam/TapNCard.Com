from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

  
    username = models.CharField(max_length=50, blank=True, default='@')
    full_name = models.CharField(max_length=100, blank=False)
    business = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    email_address = models.EmailField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    about = models.CharField(max_length=300, blank=True)
    facebook = models.URLField(blank=False, default="http://www.facebook.com/")
    instagram = models.URLField(blank=True, default="http://www.instagram.com/")
    tiktok = models.URLField(blank=True, default="http://www.tiktok.com/")
    twitter = models.URLField(blank=True, default="http://www.twitter.com/")
    linkedin = models.URLField(blank=True, default="http://www.linkedin.com/")
    paypal = models.URLField(blank=True, default="http://www.paypal.com/")
    cashapp = models.URLField(blank=True, default="http://www.cashapp.com/")
    snap = models.URLField(blank=True, default="http://www.snapchat.com/")
    discord = models.URLField(blank=True, default="http://www.discord.com/")
    twitch = models.URLField(blank=True, default="http://www.twitch.com/")
    spotify = models.URLField(blank=True, default="http://www.spotify.com/")
    apple_music = models.URLField(blank=True, default="http://www.applemusic.com/")
    sound_cloud = models.URLField(blank=True, default="http://www.soundcloud.com/")

    def __str__(self):
        return f"{self.user.username}, {self.full_name}, {self.business}, {self.phone_number}, {self.email_address}, {self.website}, {self.job_title}, {self.about}"

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.pk)])

    
    @property
    def generate_facebook_url(self):
        if self.facebook:
            return self.facebook
        return f"www.facebook.com/{self.user.username}"

    @property
    def generate_instagram_url(self):
        if self.instagram:
            return self.instagram
        return f"www.instagram.com/{self.user.username}"

    @property
    def generate_tiktok_url(self):
        if self.tiktok:
            return self.tiktok
        return f"www.tiktok.com/@{self.user.username}"

    @property
    def generate_twitter_url(self):
        if self.twitter:
            return self.twitter
        return f"www.twitter.com/{self.user.username}"

    @property
    def generate_linkedin_url(self):
        if self.linkedin:
            return self.linkedin
        return f"www.linkedin.com/in/{self.user.username}"

    @property
    def generate_paypal_url(self):
        if self.paypal:
            return self.paypal
        return f"www.paypal.me/{self.user.username}"

    @property
    def generate_cashapp_url(self):
        if self.cashapp:
            return self.cashapp
        return f"www.cash.app/${self.user.username}"

    @property
    def generate_snap_url(self):
        if self.snap:
            return self.snap
        return f"www.snapchat.com/add/{self.user.username}"

    @property
    def generate_discord_url(self):
        if self.discord:
            return self.discord
        return f"www.discord.com/users/{self.user.username}"

    @property
    def generate_twitch_url(self):
        if self.twitch:
            return self.twitch
        return f"www.twitch.tv/{self.user.username}"

    @property
    def generate_spotify_url(self):
        if self.spotify:
            return self.spotify
        return f"www.spotify.com/user/{self.user.username}"

    @property
    def generate_apple_music_url(self):
        if self.apple_music:
            return self.apple_music
        return f"www.music.apple.com/profile/{self.user.username}"

    @property
    def generate_soundcloud_url(self):
        if self.sound_cloud:
            return self.sound_cloud
        return f"www.soundcloud.com/{self.user.username}"
    


class PostImage(models.Model):

    user = models.OneToOneField(Post, on_delete=models.CASCADE)


    profile_picture = models.ImageField( upload_to='images/profile',null=True ,blank=True, default='media/images/profile/defaultBizman_5lfB6OA.jpg')
    background_banner = models.ImageField( upload_to='images/profile',null=True, blank=True, default='media/images/profile/TapNCard_Default_Profile_Banner_zZkKI0A.png')

    def __str__(self):
        return f"{self.profile_picture}, {self.background_banner}"


