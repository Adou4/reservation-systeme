# reservation/urls.py
from django.urls import path
from .views import reservation, reservation_success

urlpatterns = [
    path('reservation/', reservation, name='reservation'),
    path('reservation-success/', reservation_success, name='reservation_success'),
]
