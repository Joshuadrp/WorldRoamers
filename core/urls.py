from . import views
from django.urls import path

urlpatterns = [
    path('', views.Locations.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('register/', views.register_view, name='register'),
]