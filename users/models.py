from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

'''
This class is to help store the user profile information.
It's relationship allows each user have a unique profile.
Cloudinary is used to store the users profile picture.
'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', default='placeholder')
    surgery_type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

'''
This is a placeholder for the user model.
'''
class User(models.Model):
    pass

'''
This is a placeholder for the therapist model.
'''
class Therapist(models.Model):
    pass


"""
This tracks the user's appointment when booking.
It will track who made the appointment, the date, time,
type of appointment, notes, and status.
It will display 'appointment by the user on date entered'
"""
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)
    appointment_type = models.CharField(max_length=100, choices=[
        ('initial consultation', 'Initial Consultation'),
        ('follow up', 'Follow Up')
    ], default='initial consultation')
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    ], default='pending')
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"Appointment by {self.user} on {self.appointment_date}"

