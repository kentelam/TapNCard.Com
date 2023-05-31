from django.urls import path
from . import views
from .views import UserRegisterView, ProfileView, profile_editor


urlpatterns = [
    
path('register/', UserRegisterView.as_view(), name='register'),

path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),


path('profile/<int:pk>/edit/', views.profile_editor, name='edit'),



    
    

]