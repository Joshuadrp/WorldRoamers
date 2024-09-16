from . import views
from django.urls import path

urlpatterns = [
    path('', views.MyProfileListView.as_view(), name='profile'), #class based
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/create/', views.create_profile, name='create_profile'), #function based
]