from django.shortcuts import render
from departement.models import Departement

# Create your views here.

def departement(request):
    return render(request, 'departement.html')



def enregistrerDep(request):
    
    if request.method == "":
        nom = request.POST.get('nom')
        new_dep = Departement.objects.create(
            nomDep = nom
        )  
        
        

def modifierDep(request,id_dep):
    
    if request.method == "":
        nom = request.POST.get('nom')
        try:
            old_dep = Departement.objects.get(
                idDep = id_dep)         
            old_dep.nomDep = nom
            old_dep.save()
        except old_dep.DoesNotExist:
            return "ce departement n'existe pas"
        

        
        
def supprimerDep(id_dep):
    
    try:
        Departement.objects.filter(idDep = id_dep).delete()
    except Exception as e:
        print(f"erreur de suppression du departement {e}")
        
        
def afficherDep():
    
    try:
        all_dep = Departement.objects.all()
    except Exception as e:
        print(f"erreur d'affichage du departement {e}")
        
        
            
 
        
    