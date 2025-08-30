from django.contrib import admin
from .models import UserProfile, Appointment, Testimonials


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'surgery_type', 'created_at', 'updated_on')
    list_filter = ('surgery_type', 'created_at')
    search_fields = ('user__username', 'user__email', 'surgery_type')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'appointment_date', 'appointment_time', 'status')
    list_filter = ('status',)
    actions = ['approve_appointments']

    @admin.action(description='Approve selected appointments')
    def approve_appointments(self, request, queryset):
        queryset.update(status='confirmed')


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('user', 'testimonial', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')

