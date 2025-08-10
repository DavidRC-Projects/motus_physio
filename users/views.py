from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
import cloudinary.uploader


def index(request):
    return render(request, 'index.html')

@login_required
def booking(request):
    return render(request, 'users/booking.html')


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


@login_required
def delete_photo(request):
    if request.method == 'POST':
        user = request.user
        try:
            profile = user.userprofile
            if profile.profile_picture and "placeholder" not in str(profile.profile_picture):
                public_id = profile.profile_picture.public_id
                cloudinary.uploader.destroy(public_id)
                profile.profile_picture = 'placeholder'
                profile.save()
                messages.success(request, 'Profile picture deleted successfully!')
            else:
                messages.info(request, 'No profile picture to delete.')
        except Exception as e:
            messages.error(request, f'Failed to delete profile picture: {str(e)}')
        return redirect('profile')
    return redirect('profile')

@login_required
def surgery_type(request):
    user = request.user
    if request.method == 'POST':
        surgery_type = request.POST.get('surgery_type')
        other_surgery = request.POST.get('other_surgery')
        if surgery_type:
            profile, _ = UserProfile.objects.get_or_create(user=user)
            if surgery_type == 'other' and other_surgery:
                profile.surgery_type = other_surgery
            else:
                profile.surgery_type = surgery_type
            profile.save()
            messages.success(request, 'Surgery type updated successfully')
            return redirect('profile')
    return redirect('profile')