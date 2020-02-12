from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from datetime import date, datetime
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
        reservations = Reservation.objects.all().filter(room=room).filter(date__gte=date.today()).order_by("date")
        return render(request, "room_info.html", {"room": room, "reservations": reservations})

    def post(self, request, id):
        if request.POST.get("manage") == "Zarezerwuj":
            return redirect(f"/reservation/{id}")
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

class ReserveRoom(View):
    def get(self, request, id_room):
        room = Room.objects.get(pk=id_room)
        reservations = Reservation.objects.all().filter(room=room).filter(date__gt=date.today())
        return render(request, "reservation.html", {"room": room, "reservations": reservations})

    def post(self, request, id_room):
        if request.POST.get("manage") == "Rezerwuj":
            room = Room.objects.get(pk=id_room)
            reservations = Reservation.objects.all().filter(room=room).filter(date__gt=date.today())
            new_date = request.POST.get("date")
            comment = request.POST.get("comment")
            if new_date:
                new_date = datetime.strptime(new_date, "%Y-%m-%d").date()
                if new_date >= date.today():
                    new_reservation = Reservation.objects.filter(room=room, date=new_date)
                    if not new_reservation:
                        Reservation.objects.create(room=room, date=new_date, comment=comment)
                        return redirect("/")
                    else:
                        info = "Sala w tym dniu jest zajęta!"
                        return render(request, "reservation.html",
                                      {"room": room, "reservations": reservations, "info": info})
                else:
                    info = "Wprowadź późniejszą datę rejestracji!"
                    return render(request, "reservation.html",
                                  {"room": room, "reservations": reservations, "info": info})
            else:
                info = "Wprowadź datę rejestracji!"
                return render(request, "reservation.html",
                              {"room": room, "reservations": reservations, "info": info})
        else:
            return redirect("/")


class SearchRoom(View):
    def get(self, request):
        date = request.GET.get("date")
        name = request.GET.get("name")
        capacity = request.GET.get("capacity")
        has_projector = request.GET.get("has_projector")

        if date:
            date = datetime.strptime(date, "%Y-%m-%d").date()
            if name:
                room = Room.objects.filter(name=name, capacity__gte=capacity, has_projector=has_projector)
                if room:
                    reservations = Reservation.objects.filter(date=date, room = room)
                    if reservations:
                        info = "Brak wolnych sal dla podanych kryteriów wyszukiwania"
                        return render(request, "search.html", {"info": info})
                    else:
                        return render(request, "search.html", {"rooms": (room,)})
                else:
                    info = "Brak wolnych sal dla podanych kryteriów wyszukiwania"
                    return render(request, "search.html", {"info": info})
            else:
                rooms = Room.objects.filter(capacity__gte=capacity, has_projector=has_projector)
                rooms_info = []
                if rooms:
                    for r in rooms:
                        if not r.reservation_set.filter(date=date):
                            rooms_info.append(r)
                if rooms_info:
                    return render(request, "search.html", {"rooms": rooms_info})
                else:
                    info = "Brak wolnych sal dla podanych kryteriów wyszukiwania"
                    return render(request, "search.html", {"info": info})
        else:
            info = "Podaj datę rezerwacji"
            return render(request, "search.html", {"info": info})
