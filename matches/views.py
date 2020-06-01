from .models import Match
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from msgs.models import Message

class MatchesListView(ListView):
    model = Match
    template_name = 'matches/matches.html'
    context_object_name = 'matches'

    def get_context_data(self, **kwargs):
        context = super(MatchesListView, self).get_context_data(**kwargs)
        context['matches'] = Match.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user)).all()
        context['my_messages'] = Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user)).all().order_by('date_of_create')
        context['users'] = []
        context['my_matches'] = []
        for match in context['matches']:
            if match.user1 == self.request.user:
                context['my_matches'].append(match.user2)
            elif match.user2 == self.request.user:
                context['my_matches'].append(match.user1)
        users = list(context['my_messages'].values_list('receiver', flat=True)) + list(context['my_messages'].values_list('sender', flat=True))
        for user in users:
            if user not in context['users']:
                context['users'].append(user)
        return context
