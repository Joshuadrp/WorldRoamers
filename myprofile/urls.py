from . import views
from django.urls import path

urlpatterns = [
    path('profile/', views.MyProfile.as_view(), name='profile'), 
]