from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from utils.decorators import authorize, get_req
from chats.models import Chat

@csrf_exempt
@authorize
@get_req
def get_friends(request, *args, **kwargs):
    friends = request.user.friends.all()
    ret_friends = []
    for friend in friends:
        friend_dict = friend.to_dict()
        # friend_dict["recentMessage"] = Chat.objects.filter(from_user=)
        ret_friends.append(friend_dict)
    return JsonResponse({
        "friends": ret_friends,
    })