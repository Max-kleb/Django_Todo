from django.db import models
from todo.models import Liste 

# Create your models here.

class Tache(models.Model):
    libelle = models.CharField(max_length=10, unique=True, null=False)
    categorie = models.CharField( max_length=10 )
    horaires = models.TimeField()

    liste = models.ForeignKey(Liste, related_name="taches", on_delete=models.CASCADE)# supprimer une liste supp toute ses taches
    