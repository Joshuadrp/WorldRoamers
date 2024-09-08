from django.shortcuts import render
from django.views import generic

# Create your views here.
class Chat(generic.TemplateView):
    template_name = "message/chat.html"