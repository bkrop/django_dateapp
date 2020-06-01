from django.urls import path
from .views import MessageCreateView

urlpatterns = [
    path('new/<int:receiver_id>', MessageCreateView.as_view(), name='create_message')
]