from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Profile(models.Model):
    GENDERS = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='Date of birth', null=False, blank=False)
    gender = models.CharField(verbose_name='Gender', null=False, blank=False, choices=GENDERS,
                                max_length=5)
    description = models.TextField(null=True, blank=True, max_length=300)

    def get_age(self):
        today = date.today() 
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)) 
        return age
