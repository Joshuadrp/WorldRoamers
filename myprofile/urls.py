from . import views
from django.urls import path


urlpatterns = [
    path('', views.MyProfileListView.as_view(), name='profile'), #class based
    path('edit/', views.edit_profile, name='edit_profile'),
    path('create/', views.create_profile, name='create_profile'),
    path('delete/', views.delete_profile, name='delete_profile'),
    path('<int:pk>/', views.profile_detail, name='profile_detail'),
]