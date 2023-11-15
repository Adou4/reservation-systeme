# reservation/models.py
from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    def __str__(self):
        return f'{self.user.username} - {self.location.name} - {self.date} {self.time_start}-{self.time_end}'


