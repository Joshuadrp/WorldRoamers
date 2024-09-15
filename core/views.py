from django.shortcuts import render
from django.views import generic
from .models import Location
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class Locations(generic.ListView):
    queryset = Location.objects.all() #makes easier to get data.
    template_name = "core/home.html"

class About(generic.TemplateView):
    template_name = "core/about.html"

