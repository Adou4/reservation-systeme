# reservation/views.py
from django.shortcuts import render, redirect
from .forms import ReservationForm


def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Si votre système utilise l'authentification utilisateur
            reservation.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservation/make_reservation.html', {'form': form})


def reservation_success(request):
    return render(request, 'reservation/reservation_success.html')
