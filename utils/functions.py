import uuid

from authentication.models import *
from user.models import User

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

def verify_token(token):
    tokens = AuthToken.objects.filter(auth_token=token)

    if len(tokens) == 1:
        return True, tokens[0].user
    else:
        return False, None

def get_user_from_id(id):
    if is_valid_uuid(id):
        user = User.objects.filter(id=uuid.UUID(id))
        if len(user) > 0:
            return user.first()
        
    return None