from django.shortcuts import render

# Create your views here.

def disponibilite(request):
    return render(request, 'disponibilite.html')