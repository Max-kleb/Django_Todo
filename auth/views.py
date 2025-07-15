import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Utilisateur 

@csrf_exempt
def signup(request):

    #verification de la methode
    if request.method != 'POST':
        return JsonResponse({'error': 'methode non authorisee'}, status=405 )
    
    #verification des donnees lors du chargement
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'erreur':'requete mal formee' })
    
    email = data.get('email')
    nom = data.get('nom', '')
    mot_de_passe = data.get('mot_de_passe')

    #verification des parametres obligatoires
    if not email or not mot_de_passe:
        return JsonResponse({'erreur':'email et mot_de_passe sont obligatoires'}, status=400)

    #verification de l'unicite de l'email
    if Utilisateur.objects.filter(email=email).exists():
        return JsonResponse({'erreur':'Email deja existant'}, status=400)
    
    if len(mot_de_passe)< 6:
        return JsonResponse({'erreur':'mot de passe invalide (minimum 6 caracteres)'})
    
    #creation de l'utilisateur
    utilisateur = Utilisateur(email = email,nom=nom, mot_de_passe=mot_de_passe)
    utilisateur.save()