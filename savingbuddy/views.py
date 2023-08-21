import bcrypt

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError

from .models import User, Log

# Create your views here.

def index(request):
    return render(request, "savingbuddy/index.html", {
        "recentactivity" : Log.objects.filter(user = request.user).order_by('timestamp')[:10]
    })