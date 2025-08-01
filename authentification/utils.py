import jwt
from .models import Utilisateur

SECRET_KEY = "ma_cle_ultra_secrete"

def generate_token(user) :
    payload ={
        'user_id' : user.id,
        'email' : user.email
    }

    return jwt.encode(payload, SECRET_KEY, algorithm = 'HS256')



def verify_user (request):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return None
    
    try :
        token = auth_header.split(' ')[1]
        decoded = jwt.decode(token, SECRET_KEY, algorithms = ['HS256'])
        user_id = decoded.get('user_id')
        return Utilisateur.objects.get(id = user_id)
    
    except(jwt.ExpiredSignatureError, jwt.InvalidTokenError, IndexError):
        return None
    except Utilisateur.DoesNotExist:
        return None