from django.db import models

# Create your models here.
class Matiere(models.Model):
    
    idMat = models.AutoField(primary_key=True)
    nomMatiere = models.CharField(max_length=50)
    quotaHoraire = models.IntegerField()
    priorite = models.BooleanField()
