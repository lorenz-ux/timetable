from django.shortcuts import render
from django.http import request
# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def index(request):
    return render(request, 'index.html')


def cours(request):
    return render(request, 'cours.html')