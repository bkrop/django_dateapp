from .models import Match
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

class MatchesListView(ListView):
    model = Match
    template_name = 'matches/matches.html'
    context_object_name = 'matches'

    def get_context_data(self, **kwargs):
        context = super(MatchesListView, self).get_context_data(**kwargs)
        context['matches'] = Match.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user)).all()
        return context
