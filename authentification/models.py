from django.db import models


class Utilisateur(models.Model):
    email= models.EmailField(unique=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=10)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

