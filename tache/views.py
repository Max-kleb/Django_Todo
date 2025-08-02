from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Tache
from django.views.decorators.csrf import csrf_exempt
from todo.models import Liste

# Create your views here.

@csrf_exempt
def create_task(request):
    if request.method != 'POST' :
        return JsonResponse ({'erreur':'method not allowed'})
    try:
        data = json.loads(request.body)
        libelle = data.get("libelle")
        categorie = data.get("categorie")
        horaires = data.get("horaires")
    except:
        return JsonResponse({'erreur': 'error during data loading'})    

    if not libelle or not categorie:
        return JsonResponse ({'errreur':'libelle et categorie are required'})
    
    try:
        liste = Liste.objects.get(pk= data.get('list_id'))
        tache = Tache.objects.create(libelle=libelle, categorie = categorie, horaires=horaires, liste = liste)
        tache.save()
    except Liste.DoesNotExist:
        return JsonResponse ({'errreur':'the list doesnot exist'}, status = 404)
    except json.JSONDecodeError:
        return JsonResponse ({'errreur':'requete json mmal formule'})

    return JsonResponse ({
        'id':tache.id,
        'list_id': liste.id,
        'libelle':tache.libelle,
        'categorie':tache.categorie,
        'horaires':tache.horaires
    })

@csrf_exempt

def update_task(request,task_id):

    if request.method != 'PUT' :
        return JsonResponse ({'erreur':'method not allowed'})
    
    data = json.loads(request.body)

    try:
        tache = Tache.objects.get(pk=task_id, liste_id = data.get('list_id'))
        tache.libelle = data.get('libelle', tache.libelle)
        tache.save()

        return JsonResponse({
            'id':tache.id,
            'libelle':tache.libelle,
            'categorie':tache.categorie,
            'list_id':tache.liste.id
        })
    except Tache.DoesNotExist:
        return JsonResponse({'erreur': 'tache non trouvée'}, status=404)
    except json.JSONDecodeError :
        return JsonResponse({'erreur': 'requete json mal formule'})
    except Exception:
        return JsonResponse({'erreur': 'Unknowed error'}, status=400)
    

@csrf_exempt   

def display_task(request, list_id):
    
    if request.method != 'GET' :
        return JsonResponse ({'erreur':'method not allowed'})

    if not list_id:
        return JsonResponse ({'erreur': 'list_id requis'})
    try:
        tache = Tache.objects.filter( liste_id = list_id).values()
        return JsonResponse({
            'list_id':list_id,
            'taches': list(tache)
        }, safe=False)
    except Liste.DoesNotExist:
        return JsonResponse({'erreur': 'list not found'}, status = 404)
    except Exception as e:
        return JsonResponse({'erreur': str(e) }, status = 400)

@csrf_exempt

def delete_task(request,task_id):
    if request.method != 'DELETE' :
        return JsonResponse ({'erreur':'method not allowed'})

    if not task_id:
        return JsonResponse ({'erreur': 'list_id requis'})

    try:
        tache = Tache.objects.get(pk=task_id)
        tache.delete()
        return JsonResponse({'message': 'tache supprimée avec succès'}, status=200)
    except Tache.DoesNotExist:
            return JsonResponse({'erreur': 'tache non trouvée'}, status=404)
    except json.JSONDecodeError :
            return JsonResponse({'erreur': 'requete json mal formule'})
    except Exception as e :
            return JsonResponse({'erreur': str(e) }, status=400)