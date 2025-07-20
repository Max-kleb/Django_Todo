from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from authentification.models import Utilisateur
from .models import Liste , Tache
import json 

# recuperer les taches d'une liste precise
@csrf_exempt
def display_list(request):
    if request.method != 'GET':
        return JsonResponse({'erreur':'methode non valide !!'}, status=405)

    try:
        data = json.loads(request.body)
    except Exception as e:
        return JsonResponse({'erreur':str(e)}, status = 400)  
     
    user_id = data.get('user_id')
    if not user_id:
        return JsonResponse({'erreur':' utilisateur requis !!'})
    
    try: 
        List = Liste.objects.filter(user_id = user_id.values())
        return JsonResponse({'listes':list(List)}, safe = False) # permet a JsonRsponce de renvoyer des elements autres que des dictionnaires
    except Exception as e:
        return JsonResponse({'erreur': str(e)}, status = 400)



    
@csrf_exempt
def create_list (request):
    if request.method != 'POST':
        return JsonResponse({'erreur':'methode non valide !!'}, status=405)

    try:
        data = json.loads(request.body)
        user = Utilisateur.objects.get(pk=data["user_id"] )
        List = Liste.objects.create(nom=data["nom"], user = user)
        return JsonResponse ({
            'id':List.id,
            'nom':List.nom,
            'user_id': user.id
        }, status = 201)
    
    except Utilisateur.DoesNotExist :
        return JsonResponse({'erreur': 'user not found'}, status = 404)
    except Exception as e:
        return JsonResponse({'erreur': str(e)}, status = 400)    

@csrf_exempt
def update_list(request):
    if request.method != 'PUT':
        return JsonResponse({'erreur':'methode non valide !!'}, status=405)

    try:
        data = json.loads(request.body)
        list_id = data.get("list_id")
        List = Liste.objects.get(pk=list_id, user_id = data['user_id'])
        List.nom = data.get('nom', List.nom)
        List.save()
        return JsonResponse({
                'id': List.id,
                'nom': List.titre,
                'user_id': List.user.id 
            })
    except Liste.DoesNotExist:
            return JsonResponse({'erreur': 'Liste non trouvée'}, status=404)
    except Exception as e:
            return JsonResponse({'erreur': str(e)}, status=400)
    

@csrf_exempt
def delete_list(request):
    if request.method != 'DELETE':
        return JsonResponse({'erreur':'methode non valide !!'}, status=405)

    try:
        data = json.loads(request.body)
        list_id = data.get("list_id")
        List = List.objects.get(pk=list_id, user_id = data['user_id'])
        List.delete()
        return JsonResponse({'message': 'Liste supprimée avec succès'}, status=200)
    except Liste.DoesNotExist:
        return JsonResponse({'error': 'Liste non trouvée'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)