from django.shortcuts import render

# Create your views here.
def matiere(request):
    return render(request, "matiere.html")