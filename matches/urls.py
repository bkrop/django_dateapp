from .views import MatchesListView
from django.urls import path

urlpatterns = [
    path('', MatchesListView.as_view(), name='matches'),
]
