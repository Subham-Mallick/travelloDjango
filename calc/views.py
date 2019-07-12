from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    prop = {'name':'Subham'}

    return render(request,'home.html',prop)

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']

    prop = {'result':int(val1) + int(val2)}

    return render(request,'result.html',prop)