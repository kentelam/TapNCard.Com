from django.urls import path
from . import views
from .views import HomeView, ProfileView, ContactFormView, ThankYouView, CreateView, profile_editor


urlpatterns = [
    
    #path("", views.home, name='home'),

    path('', HomeView.as_view(), name='home'),


    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),


    path('profile/<int:pk>/edit/', views.profile_editor, name='edit'),
    

    path('thankyou/', ThankYouView.as_view(), name='thankyou' ),


    path('contact/', ContactFormView.as_view(), name='contact'),


    
        
]
