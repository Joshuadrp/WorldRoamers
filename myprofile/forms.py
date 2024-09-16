from django import forms
from .models import MyProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = MyProfile
        fields = ['name', 'surname', 'bio', 'interests']

