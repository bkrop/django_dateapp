from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDERS = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='Date of birth', null=False, blank=False)
    gender = models.CharField(verbose_name='Gender', null=False, blank=False, choices=GENDERS,
                                max_length=5)
