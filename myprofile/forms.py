from django import forms
from .models import MyProfile

class MyProfileForm(forms.ModelForm):
    class Meta:
        model = MyProfile
        fields = ['bio', 'name', 'surname', 'profile_picurl', 'countries_visited', 'interests']