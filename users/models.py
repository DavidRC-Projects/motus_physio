from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models

"""
This model is to help store the user profile information.
It's relationship allows each user have a unique profile as
it has a one to one relationship.
Cloudinary is used to store the users images.
The surgery type is a dropdown menu to allow selection of the
surgery type.
This has automatic timestamps for creation and updates.
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
