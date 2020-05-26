from django.db import models
from django.contrib.auth.models import User

class Like(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_given')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_received')
