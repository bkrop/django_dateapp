from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

class Profile(models.Model):
    GENDERS = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    SHOW_GENDERS = [
        ('Males', 'Males'),
        ('Females', 'Females'),
        ('Both', 'Both')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='Date of birth', null=False, blank=False)
    gender = models.CharField(verbose_name='Gender', choices=GENDERS, max_length=10)
    description = models.TextField(null=True, blank=True, max_length=300)
    gender_pref = models.CharField(verbose_name='Show me', choices=SHOW_GENDERS, max_length=10,
                                    default='Unspecified')

    def get_age(self):
        today = date.today() 
        age = today.year - self.date_of_birth.year - ((today.month, today.day) <
                                (self.date_of_birth.month, self.date_of_birth.day)) 
        return age

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})