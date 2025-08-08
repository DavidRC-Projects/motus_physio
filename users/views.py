from django.shortcuts import render
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