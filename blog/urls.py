from . import views
from django.urls import path

urlpatterns = [
    path('', views.Posts.as_view(), name='blog'), #django will append the empty string using urls.py in project.
]