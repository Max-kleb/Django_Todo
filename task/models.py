from django.db import models
from todolist.models import List

class Task(models.Model):
    libelle = models.CharField(max_length=10, unique=True, null=False)
    categorie = models.CharField(max_length=10)
    horaires = models.TimeField()

    liste = models.ForeignKey(List, related_name="taches", on_delete=models.CASCADE)# supprimer une liste supp toute ses taches


