from django.shortcuts import render
from .models import Message
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.db.models import Q

class MessageCreateView(CreateView):
    model = Message
    fields = ['content']
    template_name = 'msgs/create_message.html'

    def form_valid(self, form):
        form.instance.sender = self.request.user # przypisuje id zalogowanego usera do autora
        receiver = User.objects.get(id=self.kwargs['receiver_id'])
        form.instance.receiver = receiver
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(MessageCreateView, self).get_context_data(**kwargs)
        receiver = User.objects.get(id=self.kwargs.get('receiver_id'))
        context['messages'] = Message.objects.filter(Q(sender=receiver, receiver=self.request.user)|Q(sender=self.request.user, receiver=receiver)).order_by('date_of_create')
        return context
