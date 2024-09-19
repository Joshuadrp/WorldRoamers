from . import views
from django.urls import path

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('send/', views.send_message, name='send_message'),
    path('<int:pk>/', views.message_detail, name='message_detail'),
]