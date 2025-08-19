from rest_framework.views import APIView
from rest_framework.response import Response
from .models import List

from authentication.utils import verify_user

class ListView(APIView):
    def get(self, request):
        user = verify_user(request)
        if not user:
            return Response({'success': False, 'message': 'Authentification requise'}, status=401)
        listes = List.objects.filter(user=user).values()
        return Response({'success': True, 'message': 'Listes récupérées', 'listes': list(listes)})

    def post(self, request):
        user = verify_user(request)
        if not user:
            return Response({'success': False, 'message': 'Authentification requise'}, status=401)
        nom = request.data.get('nom')

        if not nom:
            return Response({'success': False, 'message': 'Nom requis'}, status=400)
        
        if List.objects.filter(nom=nom, user=user).exists():
            return Response({'success': False, 'message': 'Liste déjà existante'}, status=400)
        
        objs = List.objects.all()
        print(objs) 

        liste = List.objects.create(nom=nom, user=user)
        return Response({'success': True, 'message': 'Liste créée', 'id': liste.id, 'nom': liste.nom, 'user_id': user.id}, status=201)

    def put(self, request, list_id=None):
        user = verify_user(request)
        if not user:
            return Response({'success': False, 'message': 'Authentification requise'}, status=401)
        if list_id is None:
            return Response({'success': False, 'message': 'ID de liste requis'}, status=400)
        try:
            liste = List.objects.get(pk=list_id, user=user)
        except List.DoesNotExist:
            return Response({'success': False, 'message': 'Liste non trouvée'}, status=404)
        nom = request.data.get('nom')
        if not nom:
            return Response({'success': False, 'message': 'Nom requis'}, status=400)
        liste.nom = nom
        liste.save()
        return Response({'success': True, 'message': 'Liste mise à jour', 'id': liste.id, 'nom': liste.nom, 'user_id': user.id})

    def delete(self, request, list_id=None):
        user = verify_user(request)
        if not user:
            return Response({'success': False, 'message': 'Authentification requise'}, status=401)
        if list_id is None:
            return Response({'success': False, 'message': 'ID de liste requis'}, status=400)
        try:
            liste = List.objects.get(pk=list_id, user=user)
            liste.delete()
            return Response({'success': True, 'message': 'Liste supprimée'}, status=200)
        except List.DoesNotExist:
            return Response({'success': False, 'message': 'Liste non trouvée'}, status=404)
