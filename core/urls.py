from . import views
from django.urls import path

urlpatterns = [
    path('', views.Locations.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('login/', views.register_view, name='login'),
]