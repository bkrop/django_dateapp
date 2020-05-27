from django.shortcuts import render, redirect
from .models import Like, Dislike
from django.contrib.auth.models import User

def like(request, receiver_id):
    sender = request.user
    receiver = User.objects.get(id=receiver_id)
    Like.objects.create(sender=sender, receiver=receiver)
    return redirect('home')

def dislike(request, receiver_id):
    sender = request.user
    receiver = User.objects.get(id=receiver_id)
    Dislike.objects.create(sender=sender, receiver=receiver)
    return redirect('home')
