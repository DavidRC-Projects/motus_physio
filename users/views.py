from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
import cloudinary.uploader
from .models import Appointment


@login_required
def booking(request):
    if request.method == 'POST':
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        appointment_type = request.POST.get('appointment_type')
        notes = request.POST.get('notes')
        
        if not appointment_date or not appointment_time or not appointment_type:
            messages.error(request, 'Please fill in all required fields.')
        else:
            appointment = Appointment.objects.create(
                user=request.user,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                appointment_type=appointment_type,
                notes=notes
            )
            return redirect('booking')
    
    user_appointments = Appointment.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'user_appointments': user_appointments,
    }
    
    return render(request, 'users/booking.html', context)


@login_required
def index_booking(request):
    if request.method == 'POST':
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        appointment_type = request.POST.get('appointment_type')
        notes = request.POST.get('notes')
        
        if not appointment_date or not appointment_time or not appointment_type:
            messages.error(request, 'Please fill in all required fields.')
        else:
            appointment = Appointment.objects.create(
                user=request.user,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                appointment_type=appointment_type,
                notes=notes
            )
            messages.success(request, f'Appointment booked successfully for {appointment_date} at {appointment_time}!')
            return redirect('index')
    
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
    
    user_appointments = Appointment.objects.filter(user=user, status='confirmed').order_by('-created_at')

    context = {
        'user': user,
        'user_appointments': user_appointments,
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
def delete_appointment(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
        appointment.delete()
    return redirect('profile')


@login_required
def view_booking(request):
    user_appointments = Appointment.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'user_appointments': user_appointments,
    }
    
    return render(request, 'users/view_booking.html', context)


@login_required
def edit_appointment(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        appointment.appointment_date = appointment_date
        appointment.appointment_time = appointment_time
        appointment.save()

        messages.success(request, 'appointment has been updated!')
        
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

