from . import views
from django.urls import path

urlpatterns = [
    path('', views.Posts.as_view(), name='blog'), #django will append the empty string using urls.py in project.
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('location/<slug:location_slug>/', views.PostsByLocation.as_view(), name='posts_by_location'),
]