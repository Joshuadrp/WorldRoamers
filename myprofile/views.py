from django.views import generic
from django.views.generic import TemplateView
from .models import MyProfile

class MyProfile(generic.ListView):
    queryset = MyProfile.objects.all()
    template_name = "myprofile/myprofile.html"

class EditProfileView(TemplateView):
    template_name = "myprofile/edit_profile.html"

    
