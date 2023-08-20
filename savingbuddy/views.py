from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError

from .models import User

# Create your views here.
def authentication(request):
    return render(request, "savingbuddy/authentication.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "savingbuddy/authentication.html",{
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "savingbuddy/authentication.html")
    
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            return render(request, "savingbuddy/authentication.html",{
                "message" : "Passwords don't match."
            })
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "savingbuddy/authentication.html",{
                "message" : "Username already taken."
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect('savingbuddy/authentication.html')