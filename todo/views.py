from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from authentification.models import Utilisateur
from .models import Liste , Tache
import json 

# recuperer les taches d'une liste precise
@csrf_exempt
def display_list(request,user_id):

    if not user_id:
        return JsonResponse({'erreur':' utilisateur requis !!'})
    
    try: 
        List = Liste.objects.filter(user_id = user_id).values()
        return JsonResponse({'listes':list(List), 'user_id':user_id}, safe = False) # permet a JsonRsponce de renvoyer des elements autres que des dictionnaires
    except Exception:
        return JsonResponse({'erreur': 'Unknow error'}, status = 400)



    
@csrf_exempt
def create_list (request):
    if request.method != 'POST':
        return JsonResponse({'erreur':'method non authorisée'})

    try:
        data = json.loads(request.body)
        user = Utilisateur.objects.get(pk=data.get("user_id") )
        List = Liste.objects.create(nom=data.get("nom"), user = user)

        List.save()
        return JsonResponse ({
            'id':List.id,
            'nom':List.nom,
            'user_id': user.id
        }, status = 201)
    
    except Utilisateur.DoesNotExist :
        return JsonResponse({'erreur': 'user not found'}, status = 404)
    except json.JSONDecodeError :
        return JsonResponse({'erreur': 'requete json mal formulee'})
    

@csrf_exempt 
def update_list(request, list_id):
    if request.method != 'PUT':
        return JsonResponse({'erreur':'method non authorisée'})
    try:
        data = json.loads(request.body)
        #list_id = data.get("list_id")
        List = Liste.objects.get(pk=list_id, user_id = data.get("user_id"))
        List.nom = data.get("nom", List.nom)
        List.save()
        return JsonResponse({
                'id': List.id,
                'nom': List.nom,
                'user_id': List.user.id 
            })
    except Liste.DoesNotExist:
        return JsonResponse({'erreur': 'Liste non trouvée'}, status=404)
    except json.JSONDecodeError :
        return JsonResponse({'erreur': 'requete json mal formule'})
    except Exception:
        return JsonResponse({'erreur': 'Unknowed error'}, status=400)
    

@csrf_exempt
def delete_list(request,list_id):
    if request.method != 'DELETE':
        return JsonResponse({'erreur':'method non authorisée'})
    try:
        data = json.loads(request.body)
        List = Liste.objects.get(pk=list_id, user_id = data.get('user_id'))
        List.delete()
        return JsonResponse({'message': 'Liste supprimée avec succès'}, status=200)
    except Liste.DoesNotExist:
        return JsonResponse({'error': 'Liste non trouvée'}, status=404)
    except json.JSONDecodeError :
        return JsonResponse({'erreur': 'requete json mal formule'})
    except Exception as e :
        return JsonResponse({'error': str(e) }, status=400)
    
