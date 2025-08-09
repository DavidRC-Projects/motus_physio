from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'users/profile.html', context)

@login_required
def upload_photo(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        file = request.FILES.get('profile_picture')
        if file:
            profile.profile_picture = file
            profile.save()
        return redirect('profile')
    return render(request, 'upload_photo.html')

