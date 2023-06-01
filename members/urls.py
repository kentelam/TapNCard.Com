from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from .views import UserRegisterView, ProfileView, profile_editor


urlpatterns = [
    
path('register/', UserRegisterView.as_view(), name='register'),

path('password/', auth_views.PasswordChangeView.as_view()),

path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),


path('profile/<int:pk>/edit/', views.profile_editor, name='edit'),



    
    

]