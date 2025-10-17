from django.shortcuts import render
from matiere.models import Matiere

# Create your views here.
def matiere(request):
    render(request, "matiere.html")
    
def enregistrerMat(request):
    
    if request.method == "":
        new_mat = Matiere.objects.create(
            nomMatiere = request.POST.get('nom'),
            quotaHoraire= Matiere.POST.get('quota'),
            priorite= Matiere.POST.get('priorite')
        )
        
def modifierMat(request,id_mat):
    try:
        old_mat = Matiere.objects.get(idMat = id_mat)
        if request.method == "":
            old_mat.nomMatiere = request.POST.get('nom')
            old_mat.quotaHoraire = request.POST.get('quota')
            old_mat.priorite = request.POST.get('priorite')
            old_mat.save()
    except old_mat.DoesNotExist:
        print(f"cette matiere n'existe pas")

def supprimerMat(id_mat):
    
    try:
        Matiere.objects.filter(idMat = id_mat).delete()
    except Exception as e:
        print(f"erreur de suppression d'une matiere {e}")
        
        
def afficherMat():
    
    try:
        all_mat = Matiere.objects.all()
    except Exception as e:
        print(f"erreur d'affichage de la matiere {e}")
        
        