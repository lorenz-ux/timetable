from django.db import models

# Create your models here.
class Departement(models.Model):
    
    idDep = models.AutoField(primary_key=True)
    nomDep = models.CharField(max_length=50)