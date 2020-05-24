from django.contrib import admin
from django.urls import path, include
from .views import register, UserListView, ProfileDetailView, ProfileUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', UserListView.as_view(), name='home'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view(), name='update-profile')
]