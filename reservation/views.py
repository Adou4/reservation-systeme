# reservation/views.py
from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Si votre système utilise l'authentification utilisateur
            reservation.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservation/templates/reservation.html', {'form': form})


def reservation_success(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation/templates/reservation_success.html', {'reservations': reservations})
