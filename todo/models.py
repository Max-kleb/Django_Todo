from django.db import models
from authentification.models import Utilisateur

class Liste(models.Model):
    nom = models.CharField( unique=True , null=False)

    user = models.ForeignKey(Utilisateur, related_name ="listes", on_delete=models.CASCADE)

class Tache(models.Model):
    libelle = models.CharField( unique=True, null=False)
    categorie = models.CharField
    horaires = models.TimeField

    liste = models.ForeignKey(Liste, related_name="taches", on_delete=models.CASCADE)# supprimer une liste supp toute ses taches
    
