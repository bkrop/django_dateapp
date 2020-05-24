from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.models import User
from django.views.generic import ListView

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

    

# Create your views here.
