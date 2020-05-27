
from django.urls import path
from .views import like, dislike


urlpatterns = [
    path('like/<int:receiver_id>', like, name='like'),
    path('dislike/<int:receiver_id>', dislike, name='dislike')
]