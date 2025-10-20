from django.shortcuts import render

# Create your views here.
def classe(request):
    return render(request, 'classe.html')