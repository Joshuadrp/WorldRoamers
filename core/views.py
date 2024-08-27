from django.shortcuts import render
from django.views import generic
from .models import Location

# Create your views here.
class Locations(generic.ListView):
    queryset = Location.objects.all() #makes easier to get data.
    template_name = "location_list.html"