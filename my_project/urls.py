"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from register import views as register_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from users.models import UserProfile
from django.contrib import messages
from users.models import Appointment
from django.shortcuts import get_object_or_404

urlpatterns = [
    path('', users_views.index_booking, name='index'),
    path('profile/', users_views.profile, name='profile'),
    path('delete-photo/', users_views.delete_photo, name='delete_photo'),
    path('admin/', admin.site.urls),
    path("register/", register_views.register, name="register"),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('surgery-type/', users_views.surgery_type, name='surgery_type'),
    path('booking/', users_views.booking, name='booking'),
    path('index_booking/', users_views.index_booking, name='index_booking'),
    path('delete-appointment/<int:appointment_id>/', users_views.delete_appointment, name='delete_appointment'),
]
