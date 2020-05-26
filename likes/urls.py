
from django.urls import path
from .views import like


urlpatterns = [
    path('like/<int:receiver_id>', like, name='like')
]