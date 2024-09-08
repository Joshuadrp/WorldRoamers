from . import views
from django.urls import path

urlpatterns = [
    path('message/', views.Chat.as_view(), name='message'), 
]