from django.shortcuts import render, redirect
from .models import Like, Dislike
from django.contrib.auth.models import User
from matches.models import Match

def like(request, receiver_id):
    sender = request.user
    receiver = User.objects.get(id=receiver_id)
    Like.objects.create(sender=sender, receiver=receiver)
    if Like.objects.filter(sender=sender, receiver=receiver).exists() and Like.objects.filter(sender=receiver, receiver=sender).exists():
        Match.objects.create(user1=sender, user2=receiver)
    return redirect('home')

def dislike(request, receiver_id):
    sender = request.user
    receiver = User.objects.get(id=receiver_id)
    Dislike.objects.create(sender=sender, receiver=receiver)
    return redirect('home')
