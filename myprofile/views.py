from django.shortcuts import render
from django.views import generic
from .models import MyProfile

# Create your views here.
class MyProfile(generic.ListView):
    queryset = MyProfile.objects.all()
    template_name = "myprofile/myprofile.html"