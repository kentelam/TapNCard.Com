from django.urls import path
from . import views
from .views import HomeView, ContactFormView, ThankYouView, CreateView, search_view, about, PrivacyView, TermsView




urlpatterns = [
    
    #path("", views.home, name='home'),

    path('', HomeView.as_view(), name='home'),

    path('search/', search_view, name='search' ),    

    path('thankyou/', ThankYouView.as_view(), name='thankyou' ),


    path('contact/', ContactFormView.as_view(), name='contact'),


    path('about/', about, name='about'),

   
    path('privacy/', PrivacyView.as_view(), name='privacy'),

    path('terms/', TermsView.as_view(), name='terms'),



    
        
]
