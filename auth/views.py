import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
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



@csrf_exempt
def login(request):

    if request.method != 'POST':
        return JsonResponse({'erreur':'methode non valide'}, status=405)
    
    try:
        data = json.loads.get(request.body)

    except json.JSONDecodeError:     
        return JsonResponse({'erreur':'requet mal formee'}, status=400)

    email = data.get('email')
    mdp = data.get('mot_de_passe')

    if not email or not mdp :
        return JsonResponse({'erreur':'email et le mot de passe sont oblifatoires'}, status=400)

    try:
        utilisateur = Utilisateur.objects.get(email=email)
    except Utilisateur.DoesNotExist:
        return JsonResponse({'erreur':'Identifiants invalides'}, satus=401)    
    
    if not check_password(mdp, utilisateur.mot_de_passe):
        return JsonResponse({'message':'Connexiion reussie', 'id':utilisateur.id}, status=200)