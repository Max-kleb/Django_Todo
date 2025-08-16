import jwt
from .models import Utilisateur
from django.conf import settings

def generate_token(user) :
    payload ={
        'user_id' : user.id,
        'email' : user.email
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm = ['HS256'])



def verify_user (request):
    token = request.cookies.get('access_token')
    if not token:
        return None
    
    try :
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms = ['HS256'])
        user_id = decoded.get('user_id')
        return Utilisateur.objects.get(id = user_id)
    
    except(jwt.ExpiredSignatureError, jwt.InvalidTokenError, IndexError):
        return None
    except Utilisateur.DoesNotExist:
        return None 