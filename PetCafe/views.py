from django.shortcuts import render
from django.http import HttpResponse

#from MenuHum.forms import 
# Create your views here.

def index(request):
    return render(request, 'index.html')

def menus(request):
    return render(request, 'menus.html')