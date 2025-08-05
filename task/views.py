from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from todolist.models import List

class TaskView(APIView):
    def get(self, request):
        list_id = request.query_params.get('list_id')
        if not list_id:
            return Response({'success': False, 'message': 'list_id requis'}, status=400)
        try:
            taches = Task.objects.filter(liste_id=list_id).values()
            return Response({'success': True, 'message': 'Tâches récupérées', 'list_id': list_id, 'taches': list(taches)})
        except List.DoesNotExist:
            return Response({'success': False, 'message': 'Liste non trouvée'}, status=404)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=400)

    def post(self, request):
        libelle = request.data.get('libelle')
        categorie = request.data.get('categorie')
        horaires = request.data.get('horaires')
        list_id = request.data.get('list_id')
        if not libelle or not categorie or not list_id:
            return Response({'success': False, 'message': 'libelle, categorie et list_id sont requis'}, status=400)
        try:
            liste = List.objects.get(pk=list_id)
            tache = Task.objects.create(libelle=libelle, categorie=categorie, horaires=horaires, liste=liste)
            return Response({'success': True, 'message': 'Tâche créée', 'id': tache.id, 'list_id': liste.id, 'libelle': tache.libelle, 'categorie': tache.categorie, 'horaires': tache.horaires}, status=201)
        except List.DoesNotExist:
            return Response({'success': False, 'message': 'La liste n\'existe pas'}, status=404)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=400)

    def put(self, request, task_id):
        try:
            tache = Task.objects.get(pk=task_id, liste_id=request.data.get('list_id'))
            tache.libelle = request.data.get('libelle', tache.libelle)
            tache.categorie = request.data.get('categorie', tache.categorie)
            tache.horaires = request.data.get('horaires', tache.horaires)
            tache.save()
            return Response({'success': True, 'message': 'Tâche mise à jour', 'id': tache.id, 'libelle': tache.libelle, 'categorie': tache.categorie, 'list_id': tache.liste.id, 'horaires': tache.horaires})
        except Task.DoesNotExist:
            return Response({'success': False, 'message': 'Tâche non trouvée'}, status=404)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=400)

    def delete(self, request, task_id):
        try:
            tache = Task.objects.get(pk=task_id)
            tache.delete()
            return Response({'success': True, 'message': 'Tâche supprimée'}, status=200)
        except Task.DoesNotExist:
            return Response({'success': False, 'message': 'Tâche non trouvée'}, status=404)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=400)

