from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView
from .models import Profile
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = ProfileForm()
    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'users/register.html', context)

class UserListView(ListView):
    model = User
    template_name = 'users/home.html'
    context_object_name = 'users'

class ProfileDetailView(DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_object(self): # służy do 'uchwycenia' obiektu
        user = super().get_object()
        return user

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'users/update_profile.html'
    fields = ['description', 'gender_pref']

    def test_func(self):
        profile = self.get_object()
        if self.request.user.profile == profile:
            return True
        return False