from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from datetime import date
from reservations.models import *


class Main(View):
    def get(self, request):
        rooms = Room.objects.all()
        rooms_info = []
        for room in rooms:
            reservation = Reservation.objects.all().filter(room=room).filter(date=date.today())
            if reservation:
                rooms_info.append((room, "Zajęta"))
            else:
                rooms_info.append((room, "Wolna"))
        return render(request, "main.html", {"rooms_info": rooms_info})

    def post(self, request):
        return redirect("room/new/")


class RoomInfo(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        reservations = Reservation.objects.all().filter(room=room).filter(date__gt=date.today())
        return render(request, "room_info.html", {"room": room, "reservations": reservations})

    def post(self, request, id):
        if request.POST.get("manage") == "Zarezerwuj":
            pass
        return redirect("/")

class AddRoom(View):
    def get(self, request):
        return render(request, "add_room.html")

    def post(self, request):
        if request.POST.get("manage") == "Dodaj":
            room = Room()
            room.name = request.POST.get("name")
            room.capacity = request.POST.get("capacity")
            room.has_projector = request.POST.get("has_projector")
            room.save()
        return redirect("/")

class DeleteRoom(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        return render(request, "delete_room.html", {"room": room})

    def post(self, request, id):
        if request.POST.get("manage") == "Usuń":
            room = Room.objects.get(pk=id)
            room.delete()
        return redirect("/")


class ModifyRoom(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        return render(request, "modify_room.html", {"room": room})

    def post(self, request, id):
        if request.POST.get("manage") == "Zmień":
            room = Room.objects.get(pk=id)
            room.name = request.POST.get("name")
            room.capacity = request.POST.get("capacity")
            room.has_projector = request.POST.get("has_projector")
            room.save()
        return redirect("/")