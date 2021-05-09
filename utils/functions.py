import uuid

from authentication.models import *

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