# reservation/urls.py
from django.urls import path
from .views import make_reservation, reservation_success

urlpatterns = [
    path('make-reservation/', make_reservation, name='make_reservation'),
    path('reservation-success/', reservation_success, name='reservation_success'),
]
