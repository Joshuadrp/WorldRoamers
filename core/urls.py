from . import views
from django.urls import path

urlpatterns = [
    path('', views.Locations.as_view(), name='home'),
]