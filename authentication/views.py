import json
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Utilisateur
from .utils import verify_user, generate_token

@csrf_exempt
def signup(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Méthode non autorisée'}, status=405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Requête mal formée'}, status=400)
    
    email = data.get('email')
    name = data.get('name', '')
    password = data.get('password')
    
    if not email or not password:
        return JsonResponse({'success': False, 'message': 'Email et mot de passe sont obligatoires'}, status=400)
    
    if Utilisateur.objects.filter(email=email).exists():
        return JsonResponse({'success': False, 'message': 'Email déjà existant'}, status=400)
   
    if len(password) < 6:
        return JsonResponse({'success': False, 'message': 'Mot de passe invalide (minimum 6 caractères)'}, status=400)
    
    user = Utilisateur(email=email, name=name, password=password)
    user.set_password(password)
    user.save()

    token = generate_token(user)
    
    response = JsonResponse({'success': True, 'message': 'Inscription réussie'})

    response.set_cookie(
        key='access_token',
        value=token,
        httponly=True,
        secure=not settings.DEBUG,
        samesite='Lax',
        max_age=24 * 3600
    )
    # return JsonResponse({'success': True, 'message': 'Inscription réussie', 'token': token}, status=201)



@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Méthode non autorisée'}, status=405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Requête mal formée'}, status=400)
    
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return JsonResponse({'success': False, 'message': 'Email et mot de passe sont obligatoires'}, status=400)
    
    try:
        user = Utilisateur.objects.get(email=email)

        if not user or not user.checkPassword(password):
            raise Utilisateur.DoesNotExist
    except Utilisateur.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Email ou mot de passe incorrect'}, status=404)
    
    
    token = generate_token(user)

    response = JsonResponse({'success': True, 'message': 'Connexion etablie'})
    response.set_cookie(
        key='access_token',
        value=token,
        httponly=True,
        secure=not settings.DEBUG,
        samesite='Lax',
        max_age=24 * 3600
    )

    return response
    # return JsonResponse({'success': True, 'message': 'Connexion etablie', 'token': token}, status=200)
    
 

@csrf_exempt
def profile(request):
    user = verify_user(request)
    if not user:
        return JsonResponse({'success': False, 'message': 'Authentification requise'}, status=401)
    return JsonResponse({'success': True, 'message': f'Bienvenue {user.email}', 'user_id': user.id}, status=200)