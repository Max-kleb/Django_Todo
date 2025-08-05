from django.db import models
from django.contrib.auth.hashers import make_password , check_password


class Utilisateur(models.Model):
    email= models.EmailField(unique=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=128)
    
    def set_password(self,password):
        self.password = make_password(password)
    
    def checkPassword(self, password_hash):
        return check_password(password_hash, self.password )




   

