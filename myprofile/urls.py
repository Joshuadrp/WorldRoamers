from . import views
from django.urls import path

urlpatterns = [
    path('', views.MyProfileListView.as_view(), name='profile'), #class based
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'), #function based
]