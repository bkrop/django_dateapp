from django.shortcuts import render, redirect, get_object_or_404
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

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/home.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs) # get the default context data
        context['likes'] = self.request.user.likes_given.all().values_list('receiver', flat=True) # add extra field to the context
        context['dislikes'] = self.request.user.dislikes_given.all().values_list('receiver', flat=True)
        return context

class ProfileDetailView(LoginRequiredMixin, DetailView): # domyślnie zwraca obiekt o nazwie 'object', wtedy używam w template np.object.gender
    model = Profile
    template_name = 'users/profile.html'

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'users/update_profile.html'
    fields = ['description', 'gender_pref', 'avatar']

    def test_func(self):
        profile = self.get_object()
        if self.request.user.profile == profile:
            return True
        return False