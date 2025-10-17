from django.shortcuts import render
from django.http import request
# Create your views here.

def dashboard(request):
<<<<<<< HEAD
    return render(request, 'dashoard.html')
=======
    return render(request, 'dashboard.html')
>>>>>>> 59b55b3 (Ajout du login)


def cours(request):
    return render(request, 'cours.html')