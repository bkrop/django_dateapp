from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class DateInput(forms.DateInput): # służy do wstawienia typu formy jako date
    input_type = 'date'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'date_of_birth': DateInput(),
            'gender_pref': forms.RadioSelect
        }
        fields = ['date_of_birth', 'gender', 'description', 'gender_pref']
        