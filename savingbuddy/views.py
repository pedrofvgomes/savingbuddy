from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from savingbuddy.models import User, Log


# Create your views here.

def index(request):
    return render(request, "savingbuddy/index.html", {
        "recentactivity" : [0]
    })

def authentication(request):
    return render(request, 'savingbuddy/authentication.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return redirect('authentication')
    else:
        return redirect('authentication')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2 or username == "":
            return redirect('authentication')
        
        try:
            user = User.objects.create_user(username = username, password = password)
            user.save()
        except IntegrityError:
            return authentication(request)
        return redirect('index')
    else:
        return authentication(request)
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))