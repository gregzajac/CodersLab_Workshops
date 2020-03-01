from django.shortcuts import render
from django.views.generic import ListView
from MyRent.models import Flat


class FlatListView(ListView):
    model = Flat
