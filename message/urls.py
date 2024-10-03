from . import views
from django.urls import path

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('send/<int:recipient_id>/', views.send_message, name='send_message'),
    path('<int:message_id>/', views.message_detail, name='message_detail'),
]