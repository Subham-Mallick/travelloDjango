from django.shortcuts import render, redirect
from .models import Destination
# Create your views here.

def index(request):

    prop = Destination.objects.all()
    return render(request,"index.html",{'prop':prop})

def mumbai(request):
    if request.user.is_authenticated:
        return render(request,'mumbai.html')
    else:
        return redirect('login')

def bengaluru(request):
    if request.user.is_authenticated:
        return render(request,'bengaluru.html')
    else:
        return redirect('login')

def pune(request):
    if request.user.is_authenticated:
        return render(request,'pune.html')
    else:
        return redirect('login')

def hyderabad(request):
    if request.user.is_authenticated:
        return render(request,'hyderabad.html')
    else:
        return redirect('login')
