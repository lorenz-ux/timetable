from django.db import models
from departement.models import Departement
# Create your models here.
class Enseignant(models.Model):
    
    idEns = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateNaiss = models.DateField()
    grade = models.CharField(max_length=50)
    AnneeExp = models.IntegerField()
    sexe = models.CharField(max_length=10)
    domicile = models.CharField(max_length=50)
    diplome = models.CharField(max_length=20)
    idDep = models.ForeignKey(Departement, on_delete=models.CASCADE)
    