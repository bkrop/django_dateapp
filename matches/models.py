from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches2')
