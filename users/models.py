from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models

"""
This model is to help store the user profile information.
The surgery type is a dropdown menu to allow selection of the
surgery type.
This has automatic timestamps for creation and updates.
- :model:`auth.User` - OneToOneField relationship, each user
has exactly one profile.
- :model:`cloudinary.CloudinaryField` - Stores profile images
with automatic cloud hosting.
"""


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', default='placeholder')
    surgery_type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


"""
Represents an appointment booked by the user.
This model tracks the user's appointment when booking.
It will track who made the appointment, the date, time,
type of appointment, notes, and status.
appointment_type can be initial consultation or follow up.
This has automatic timestamps for creation and updates.
It will display a string of 'Appointment by <user> on <date>'
- :model:`auth.User` - ForeignKey relationship, each user can
have multiple appointments.
- :view:`users.views.booking` - Returns appointment data
for booking form.
- :view:`users.views.view_booking` - Returns appointments
for calendar display.
- :view:`users.views.edit_appointment` - Returns appointment
data for editing.
- :view:`users.views.delete_appointment` - Returns appointment
data for deletion.
"""


class Appointment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)
    appointment_type = models.CharField(
        max_length=100,
        choices=[
            ('initial consultation', 'Initial Consultation'),
            ('follow up', 'Follow Up')
        ],
        default='initial consultation'
    )
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed')
        ],
        default='pending'
    )
    needs_approval = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True
    )

    def __str__(self):
        return f"Appointment by {self.user} on {self.appointment_date}"


"""
This model stores messages between users and practitioners.
Each message is linked to a user.
The 'message' stores the content of the message.
The 'reply' is a boolean field to track if the message is a reply.
The 'parent_message' allows one message to have multiple replies.
The created_ at stores the timestamp when the message was created.
The messages are ordered by most recent first using the class Meta.
It will display a string that displays 'Messages from <username>: <subject>'.
- :model:`auth.User` - ForeignKey relationship, each user can have
multiple messages.
- :model:`users.Message` - ForeignKey for message replies.
- :view:`users.views.message_practitioner` - Returns messages for
contact page display.
- :view:`users.views.reply_to_message` - Returns message data for
reply functionality.
- :view:`users.views.delete_message` - Returns message data for deletion.
"""


class Message(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    subject = models.CharField(max_length=150, blank=False)
    message = models.TextField(blank=False)
    reply = models.BooleanField(default=False)
    parent_message = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.user.username}: {self.subject}"


"""
This model stores testimonials submitted by users.
Each testimonial is linked to a specific user.
The 'testimonial' stores the actual feedback text provided by the user.
The 'created_at' automatically records the date and time when the
testimonial was first created.
The 'updated_at' automatically updates whenever the testimonial is modified.
The testimonials are ordered by creation date in descending order
(newest first).
It will display a string that displays 'Testimonial by <username>'.
- :model:`auth.User` - ForeignKey relationship, each user can have
multiple testimonials.
- :view:`users.views.testimonials` - Returns testimonials for testimonials
page display.
- :view:`users.views.delete_testimonial` - Returns testimonial data
for deletion.
"""


class Testimonials(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='testimonials'
    )
    testimonial = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Testimonial by {self.user.username}"
