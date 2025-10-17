from django.shortcuts import render
from django.http import request

# Create your views here.


def login(request):

    return render(request, "login.html")
