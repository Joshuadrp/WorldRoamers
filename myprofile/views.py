from django.views import generic
from django.shortcuts import render, redirect
from .models import MyProfile
from .forms import ProfileForm

class MyProfileListView(generic.ListView):
    queryset = MyProfile.objects.all()
    template_name = "myprofile/myprofile.html"

def edit_profile(request):
    profile = MyProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'myprofile/edit_profile.html', {'form': form})

    
