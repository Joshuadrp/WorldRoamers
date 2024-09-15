from . import views
from django.urls import path

urlpatterns = [
    path('', views.MyProfile.as_view(), name='profile'), 
    path('profile/edit/', views.EditProfileView.as_view(), name='edit_profile'),
]