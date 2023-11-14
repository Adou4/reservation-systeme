# reservation/forms.py
from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['location', 'date', 'time_start', 'time_end']
