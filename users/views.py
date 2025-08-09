from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            profile, _ = UserProfile.objects.get_or_create(user=user)
            profile.profile_picture = profile_picture
            profile.save()
            messages.success(request, 'Profile picture updated successfully')
            return redirect('profile')

    context = {
        'user': user,
    }
    return render(request, 'users/profile.html', context)


