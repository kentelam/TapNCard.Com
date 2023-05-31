from django.urls import path
from . import views
from .views import HomeView, ContactFormView, ThankYouView, CreateView




urlpatterns = [
    
    #path("", views.home, name='home'),

    path('', HomeView.as_view(), name='home'),
    

    path('thankyou/', ThankYouView.as_view(), name='thankyou' ),


    path('contact/', ContactFormView.as_view(), name='contact'),


    
        
]
