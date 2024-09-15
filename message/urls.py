from . import views
from django.urls import path

urlpatterns = [
    path('', views.Chat.as_view(), name='message'), 
]