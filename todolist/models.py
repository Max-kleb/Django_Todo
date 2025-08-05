from django.db import models
from authentication.models import Utilisateur

class List(models.Model):
    nom = models.CharField( max_length=10 ,unique=True , null=False)

    user = models.ForeignKey(Utilisateur, related_name ="listes", on_delete=models.CASCADE)
