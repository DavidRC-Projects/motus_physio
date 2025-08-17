from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
import cloudinary.uploader
from .models import Appointment, Message, Testimonials
from datetime import date
from calendar import monthrange


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
            # Check if this time slot is already booked
            existing_appointment = Appointment.objects.filter(
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).first()
            
            if existing_appointment:
                messages.error(request, 'This time slot is already booked. Please choose a different time.')
            else:
                appointment = Appointment.objects.create(
                    user=request.user,
                    appointment_date=appointment_date,
                    appointment_time=appointment_time,
                    appointment_type=appointment_type,
                    notes=notes
                )
                messages.success(request, f'Appointment booked successfully for {appointment_date} at {appointment_time}!')
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
            # Check if this time slot is already booked
            existing_appointment = Appointment.objects.filter(
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).first()
            
            if existing_appointment:
                messages.error(request, 'This time slot is already booked. Please choose a different time.')
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
def edit_appointment(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        
        # Check if this time slot is already booked by another appointment
        existing_appointment = Appointment.objects.filter(
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).exclude(id=appointment_id).first()  # Exclude the current appointment being edited
        
        if existing_appointment:
            messages.error(request, 'This time slot is already booked. Please choose a different time.')
        else:
            appointment.appointment_date = appointment_date
            appointment.appointment_time = appointment_time
            appointment.save()
            messages.success(request, 'Appointment has been updated!')
        
    return redirect('view_booking')


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


@login_required
def view_booking(request):
    user_appointments = Appointment.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'user_appointments': user_appointments,
    }
    
    return render(request, 'users/view_booking.html', context)


def booking_calendar_view(request):
    month = int(request.GET.get('month', date.today().month))
    year = int(request.GET.get('year', date.today().year))

    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1

    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    month_name = month_names[month - 1]
    days_in_month = monthrange(year, month)[1]

    # Get current user's appointments for the selected month
    user_appointments = Appointment.objects.filter(
    user=request.user,
    appointment_date__year=year,
    appointment_date__month=month
    ).order_by('appointment_date')

    # Create list of days that have appointments (for calendar display)
    booked_days = [appointment.appointment_date.day for appointment in user_appointments]


    context = {
        'month': month,
        'year': year,
        'month_name': month_name,
        'days_in_month': days_in_month,
        'booked_days': booked_days,
        'user_appointments': user_appointments,
    }

    return render(request, 'users/view_booking.html', context)


@login_required
def message_practitioner(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if subject and message:
            Message.objects.create(
                user=request.user,
                subject=subject,
                message=message,
                reply=False
            )
            messages.success(request, 'Your message has been sent to the practitioner!')
            return redirect('message_practitioner')
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    user_messages = Message.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'user_messages': user_messages,
    }
    
    return render(request, 'users/message_practitioner.html', context)


def testimonials(request):
    if request.method == 'POST':
        testimonial_text = request.POST.get('testimonial')
        if testimonial_text:
            Testimonials.objects.create(
                user=request.user,
                testimonial=testimonial_text
            )
            messages.success(request, 'Thank you! Your testimonial has been added.')
            return redirect('testimonials')
    
    # Get all testimonials from the database, ordered by newest first
    testimonials = Testimonials.objects.all().order_by('-created_at')
    
    context = {
        'testimonials': testimonials,
    }
    
    return render(request, 'users/testimonials.html', context)


