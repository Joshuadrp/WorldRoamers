from django.shortcuts import render
from django.views import generic

# Create your views here.
class MyProfile(generic.TemplateView):
    template_name = "myprofile/myprofile.html"