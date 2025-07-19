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
    name = data.get('name', '')
    password = data.get('password')

    #verification des parametres obligatoires
    if not email or not password:
        return JsonResponse({'erreur':'email et password sont obligatoires'}, status=400)

    #verification de l'unicite de l'email
    if Utilisateur.objects.filter(email = email).exists():
        return JsonResponse({'erreur':'Email deja existant'}, status=400)
    
    if len(password)< 6:
        return JsonResponse({'erreur':'mot de passe invalide (minimum 6 caracteres)'})
    
    #creation de l'user
    user = Utilisateur(email = email,name=name, password=password)
    user.save()
    return JsonResponse({'message':'signup reussi !!'}, status=200)



@csrf_exempt
def login(request):

    if request.method != 'POST':
        return JsonResponse({'erreur':'methode non valide'}, status=405)
    
    try:
        data = json.loads(request.body)

    except json.JSONDecodeError:     
        return JsonResponse({'erreur':'requete mal formee'}, status=400)

    email = data.get('email')
    mdp = data.get('password')

    if not email or not mdp :
        return JsonResponse({'erreur':'email et le mot de passe sont obligatoires'}, status=400)

    try:
        user = Utilisateur.objects.get(email = email)
    except Utilisateur.DoesNotExist:
        return JsonResponse({'erreur':'Identifiants invalides'}, status=401)    
    
    if not check_password(mdp, user.password):
        return JsonResponse({'erreur':'Mot de passe ne correspond pas'}, status=401)
    
    else :
        return JsonResponse({'message':'Connexion etablie', 'id':user.id}, status=200)