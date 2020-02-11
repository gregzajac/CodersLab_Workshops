from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=128)
    capacity = models.SmallIntegerField()
    has_projector = models.BooleanField()


class Reservation(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField()
