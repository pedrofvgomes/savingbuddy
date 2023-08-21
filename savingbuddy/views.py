from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError

from savingbuddy.models import User, Log

# Create your views here.

def index(request):
    return render(request, "savingbuddy/index.html", {
        "recentactivity" : [0]
    })

def profile(request):
    if not request.user.is_authenticated:
        return redirect('authentication')
    
    return render(request, 'savingbuddy/profile.html', {
        "user" : request.user
    })

def authentication(request):
    return render(request, "savingbuddy/authentication.html")

def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']

        user = authenticate(request, username = username, password = password)

        if user is None:
            return redirect('authentication')
        
        login(request, user)
        return redirect('index')
    
    return authentication(request)

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2 or len(User.objects.filter(username = username)) > 0:
            return authentication(request)
        
        try:
            user = User.objects.create_user(username, password)
            user.save()
        except IntegrityError:
            return authentication(request)
        login(request, user)
        return redirect('index')
    else:
        return authentication(request)
