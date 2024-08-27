from django.shortcuts import render
from django.views import generic
from .models import Location

# Create your views here.
class Locations(generic.ListView):
    model = Location