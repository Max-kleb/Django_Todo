from django.db import models

# Create your models here.
# il ya le type date ?, c'est preferable de mettre horaire come un caractere ou comme un integer ?
# je viens de voir qu'il ya un type time 


# je songeais aussi à ajouter un champs. quel champs? un champs qui va montrer l'importance de la tache , uun truc comme ca 

# considerons pour
# le moment que categorie fais cela. ou alors tu peux changer categorie tu met pririté

# re. j'avais perdu le sync
# dacc , jai bien defini le model? yep

# categorie peux etre enum
# j'ai ask a copilot de transformer mais ca me parait bizarre donc laissons d'abord charField
# go commencer les routes maintenant

#on ne lie pas les class ?

# ahn oui. lie alors
# je sais pas comment m'y prendre
# ca m'a l'ere plus simple qu'avec flask

# yep. c'est presque la même chose pour les relations 1 a plusieurs

class Liste(models.Model):
    nom = models.CharField( unique=True , null=False)


class Tache(models.Model):
    libelle = models.CharField( unique=True, null=False)
    categorie = models.CharField
    horaires = models.TimeField

    liste = models.ForeignKey(Liste, related_name="taches", on_delete=models.CASCADE)# supprimer une liste supp toute ses taches
    

    # go sur les routes maintenant
    # dacc
    # je dois d'abord definir les vues non ?