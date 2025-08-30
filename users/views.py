from calendar import monthrange
from datetime import date
import cloudinary.uploader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Appointment, Message, Testimonials, UserProfile


@login_required
def booking(request):
    """
    Handle appointment booking for authenticated users.

    **Context**

    ``user_appointments``
        All appointments for the current user, ordered by creation date.

    **Template:**

    :template:`users/booking.html`
    """
    if request.method == 'POST':
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        appointment_type = request.POST.get('appointment_type')
        notes = request.POST.get('notes')

        if (not appointment_date or not appointment_time or
                not appointment_type):
            messages.error(
                request,
                'Please fill in all required fields.'
            )
        else:
            existing_appointment = Appointment.objects.filter(
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).first()

            if existing_appointment:
                messages.error(
                    request,
                    'This time slot is already booked. '
                    'Please choose a different time.'
                )
            else:
                appointment = Appointment.objects.create(
                    user=request.user,
                    appointment_date=appointment_date,
                    appointment_time=appointment_time,
                    appointment_type=appointment_type,
                    notes=notes
                )
                messages.success(
                    request,
                    f'Appointment booked successfully for {appointment_date} '
                    f'at {appointment_time}!'
                )
                return redirect('booking')

    user_appointments = (
        Appointment.objects.filter(user=request.user)
        .order_by('-created_at')
    )

    context = {
        'user_appointments': user_appointments,
    }

    return render(request, 'users/booking.html', context)


@login_required
def index_booking(request):
    """
    Handle appointment booking from the home page.

    **Template:**

    :template:`index.html`
    """
    if request.method == 'POST':
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        appointment_type = request.POST.get('appointment_type')
        notes = request.POST.get('notes')

        if (not appointment_date or not appointment_time or
                not appointment_type):
            messages.error(
                request,
                'Please fill in all required fields.'
            )
        else:
            existing_appointment = Appointment.objects.filter(
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).first()

            if existing_appointment:
                messages.error(
                    request,
                    'This time slot is already booked. '
                    'Please choose a different time.'
                )
            else:
                Appointment.objects.create(
                    user=request.user,
                    appointment_date=appointment_date,
                    appointment_time=appointment_time,
                    appointment_type=appointment_type,
                    notes=notes
                )
                messages.success(
                    request,
                    f'Appointment booked successfully for {appointment_date} '
                    f'at {appointment_time}!'
                )
                return redirect('index')

    return render(request, 'index.html')


@login_required
def profile(request):
    """
    Display and update user profile information.

    **Context**

    ``user``
        The current authenticated user.
    ``user_appointments``
        Confirmed appointments for the current user, ordered by creation date.

    **Template:**

    :template:`users/profile.html`
    """
    user = request.user

    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            profile, _ = UserProfile.objects.get_or_create(user=user)
            profile.profile_picture = profile_picture
            profile.save()
            messages.success(
                request,
                'Profile picture updated successfully'
            )
            return redirect('profile')

    user_appointments = (
        Appointment.objects.filter(user=user, status='confirmed')
        .order_by('-created_at')
    )

    context = {
        'user': user,
        'user_appointments': user_appointments,
    }
    return render(request, 'users/profile.html', context)


@login_required
def delete_photo(request):
    """
    Delete user's profile picture from Cloudinary storage.

    **Template:**

    Redirects to profile page after deletion.
    """
    if request.method == 'POST':
        user = request.user
        try:
            profile = user.userprofile
            if (profile.profile_picture and
                    "placeholder" not in str(profile.profile_picture)):
                public_id = profile.profile_picture.public_id
                cloudinary.uploader.destroy(public_id)
                profile.profile_picture = 'placeholder'
                profile.save()
                messages.success(
                    request,
                    'Profile picture deleted successfully!'
                )
            else:
                messages.info(
                    request,
                    'No profile picture to delete.'
                )
        except Exception as e:
            messages.error(
                request,
                f'Failed to delete profile picture: {str(e)}'
            )
        return redirect('profile')


@login_required
def delete_appointment(request, appointment_id):
    """
    Delete a specific appointment for the authenticated user.

    **Context**

    ``appointment_id``
        The ID of the appointment to delete.

    **Template:**

    Redirects to profile page after deletion.
    """
    if request.method == 'POST':
        appointment = get_object_or_404(
            Appointment, id=appointment_id, user=request.user
        )
        appointment.delete()
    return redirect('profile')


@login_required
def edit_appointment(request, appointment_id):
    """
    Edit an existing appointment for the authenticated user.
    Prevents users from booking the same time slot twice.

    **Context**

    ``appointment_id``
        The ID of the appointment to edit.

    **Template:**

    Redirects to view_booking page after editing.
    """
    if request.method == 'POST':
        appointment = get_object_or_404(
            Appointment, id=appointment_id, user=request.user
        )
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        existing_appointment = (
            Appointment.objects.filter(
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).exclude(id=appointment_id).first()
        )

        if existing_appointment:
            messages.error(
                request,
                'This time slot is already booked. '
                'Please choose a different time.'
            )
        else:
            appointment.appointment_date = appointment_date
            appointment.appointment_time = appointment_time
            appointment.status = 'pending'
            appointment.needs_approval = True
            appointment.save()
            messages.success(
                request,
                'Appointment updated! Changes require admin approval.'
            )

    return redirect('view_booking')


@login_required
def surgery_type(request):
    """
    Update user's surgery type in their profile.

    **Template:**

    Redirects to profile page after updating.
    """
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
            messages.success(
                request,
                'Surgery type updated successfully'
            )
            return redirect('profile')
    return redirect('profile')


@login_required
def view_booking(request):
    """
    Display all appointments for the authenticated user.

    **Context**

    ``user_appointments``
        All appointments for the current user, ordered by creation date.

    **Template:**

    :template:`users/view_booking.html`
    """
    user_appointments = (
        Appointment.objects.filter(user=request.user)
        .order_by('-created_at')
    )

    context = {
        'user_appointments': user_appointments,
    }

    return render(request, 'users/view_booking.html', context)


@login_required
def booking_calendar_view(request):
    """
    Display a calendar view of user's appointments for a specific month.

    **Context**

    ``month``
        The month number (1-12) to display.
    ``year``
        The year to display.
    ``month_name``
        The full name of the month.
    ``days_in_month``
        Total number of days in the month.
    ``booked_days``
        List of days that have appointments.
    ``user_appointments``
        All appointments for the current user in the selected month.

    **Template:**

    :template:`users/view_booking.html`
    """
    month = int(request.GET.get('month', date.today().month))
    year = int(request.GET.get('year', date.today().year))

    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1

    month_names = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    month_name = month_names[month - 1]
    days_in_month = monthrange(year, month)[1]
    current_month_appointments = (
        Appointment.objects.filter(
            user=request.user,
            appointment_date__year=year,
            appointment_date__month=month
        )
    )

    approval_appointments = Appointment.objects.filter(
        user=request.user,
        needs_approval=True
    )

    user_appointments = (
        current_month_appointments | approval_appointments
    ).distinct().order_by('appointment_date')

    booked_days = [
        appointment.appointment_date.day
        for appointment in current_month_appointments
    ]

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
    """
    Handle sending messages to practitioners and display user's message
    history.

    **Context**

    ``user_messages``
        All messages sent by the current user, ordered by creation date.

    **Template:**

    :template:`users/message_practitioner.html`
    """
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
            messages.success(
                request,
                'Your message has been sent to the practitioner!'
            )
            return redirect('message_practitioner')
        else:
            messages.error(
                request,
                'Please fill in all required fields.'
            )

    user_messages = (
        Message.objects.filter(user=request.user)
        .order_by('-created_at')
    )

    context = {
        'user_messages': user_messages,
    }

    return render(request, 'users/message_practitioner.html', context)


@login_required
def therapist_dashboard(request):
    """
    Display dashboard for therapists to view all appointments and patient
    messages.

    **Context**

    ``appointments``
        All appointments in the system, ordered by creation date.
    ``messages``
        All unread patient messages, ordered by creation date.

    **Template:**

    :template:`users/therapist_dashboard.html`
    """
    if not request.user.is_staff:
        messages.error(
            request,
            'Access denied. Therapist only.'
        )
        return redirect('index')

    all_appointments = (
        Appointment.objects.all()
        .order_by('-created_at')
    )
    all_messages = (
        Message.objects.filter(reply=False)
        .order_by('-created_at')
    )

    context = {
        'appointments': all_appointments,
        'messages': all_messages,
    }

    return render(request, 'users/therapist_dashboard.html', context)


@login_required
def reply_to_message(request, message_id):
    """
    Allow therapists to reply to patient messages.

    **Context**

    ``message_id``
        The ID of the message to reply to.

    **Template:**

    Redirects to therapist dashboard after replying.
    """
    if request.method == 'POST':
        reply_text = request.POST.get('reply_message')
        if reply_text:
            original_message = get_object_or_404(
                Message, id=message_id
            )
            Message.objects.create(
                user=request.user,
                subject=f"Re: {original_message.subject}",
                message=reply_text,
                reply=True,
                parent_message=original_message
            )

            original_message.reply = True
            original_message.save()
            messages.success(
                request,
                'Reply sent!'
            )
            return redirect('therapist_dashboard')

    return redirect('therapist_dashboard')


@login_required
def delete_message(request, message_id):
    """
    Delete a specific message for the authenticated user.

    **Context**

    ``message_id``
        The ID of the message to delete.

    **Template:**

    Redirects to message practitioner page after deletion.
    """
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    messages.success(
        request,
        'Message deleted successfully.'
    )
    return redirect('message_practitioner')


def testimonials(request):
    """
    Handle creating, displaying, and deleting user testimonials.

    **Context**

    ``testimonials``
        All testimonials in the system, ordered by creation date.

    **Template:**

    :template:`users/testimonials.html`
    """
    if request.method == 'POST':
        testimonial_text = request.POST.get('testimonial')
        if testimonial_text:
            Testimonials.objects.create(
                user=request.user,
                testimonial=testimonial_text
            )
            messages.success(
                request,
                'Thank you! Your testimonial has been added.'
            )
            return redirect('testimonials')

        delete_id = request.POST.get('delete_testimonial')
        if delete_id:
            testimonial = Testimonials.objects.get(
                id=delete_id, user=request.user
            )
            testimonial.delete()
            messages.success(
                request,
                'Testimonial deleted.'
            )
            return redirect('testimonials')

    testimonials = (
        Testimonials.objects.all()
        .order_by('-created_at')
    )

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'users/testimonials.html', context)
