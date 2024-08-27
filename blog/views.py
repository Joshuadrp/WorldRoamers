from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class Posts(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/posts.html"

