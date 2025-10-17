from django.shortcuts import render
from classe.models import Classe

# Create your views here.
def classe(request):
    render(request, 'classe.html')
    
def enregistrerClass(request):
    
    if request.method == "":
        nom = request.POST.get('nomClass')
        new_class = Classe.objects.create(
            nomClass = nom
        )  
        

def modifierClass(request,id_class):
    
    if request.method == "":
        nom = request.POST.get('nomClass')
        try:
            old_class = Classe.objects.get(
                idClass = id_Class) 
        except old_class.DoesNotExist:
            return "cette classe n'existe pas"
        
        old_class.nomClass = nom
        old_class.save()
        
        
def supprimerClass(id_class):
    
    try:
        Classe.objects.filter(idClass = id_class).delete()
    except Exception as e:
        print(f"erreur de suppression de la classe {e}")
        
        
def afficherClass():
    
    try:
        all_class = Classe.objects.all()
    except Exception as e:
        print(f"erreur d'affichage des classes {e}")
        
    