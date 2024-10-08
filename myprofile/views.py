from django.views import generic
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import MyProfile
from .forms import ProfileForm

class MyProfileListView(generic.ListView):
    queryset = MyProfile.objects.all()
    template_name = "myprofile/myprofile.html"

def edit_profile(request):
    profile = MyProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile edited successfully!')
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'myprofile/edit_profile.html', {'form': form})


def create_profile(request):
    
    profile = MyProfile.objects.filter(user=request.user).first()  
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.user = request.user  
            form_instance.save()  
            messages.success(request, 'Profile created successfully!')
            return redirect('profile')  
    else:
        form = ProfileForm(instance=profile)  
    
    return render(request, 'myprofile/create_profile.html', {'form': form})


def delete_profile(request):
    profile = MyProfile.objects.get(user=request.user)

    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('home')
    else:
        return render(request, 'myprofile/delete_profile.html', {'profile': profile})

def profile_detail(request, pk):
    user_profile = get_object_or_404(MyProfile, user__pk=pk)
    return render(request, 'myprofile/myprofile.html', {'user_profile': user_profile})



        
    
