from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from .views import UserRegisterView, AddProfileView, ProfileView, profile_editor, PasswordChangeView


urlpatterns = [
    
path('register/', UserRegisterView.as_view(), name='register'),

#path('change_password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name ='change_password'),

#path('change_password/', PasswordsChangeView.as_view(template_name='registration/password_change_form.html'), name ='change_password'),

path('change_password/', views.change_password, name ='change_password'),

path('add-profile/<int:pk>/', AddProfileView.as_view(), name='create-profile'),

path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),


path('profile/<int:pk>/edit/', views.profile_editor, name='edit'),


path('petprofile/', views.pet_profile, name='pets'),

    
    

]
