from django.http import JsonResponse
from django.db.models import Q
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
        recent_chat = Chat.objects.filter(Q(from_user=request.user, to_user=friend) | Q(from_user=friend, to_user=request.user)).last()
        
        message = "Start Chat"
        if recent_chat:
            message = recent_chat.message
        
        friend_dict["recentMessage"] = message
        ret_friends.append(friend_dict)
    return JsonResponse({
        "friends": ret_friends,
    })