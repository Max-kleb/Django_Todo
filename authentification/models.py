from django.db import models


class Utilisateur(models.Model):
    email= models.EmailField(unique=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=10)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


# garrrrrr
# lance la commande la dans le terminal norr



# dans le requirement il faut mettre django

# et ca demande aussi une version ou un range de cersion donc j ai mis >= la version actuelle

# a quel niveau?
# comment tu mats dans le reqquir django >=5.2 ?
# je change et je met 3 ?



# pourquoi tu veux changer?
# ta version actu ce n'est pas 5.2
# non 
# tu as access a mom

# ce n'est même pas important. fais pip install -r reqi    
# il ya des erreurs 
# # je ne trouve meme plus django dans pip list
