import json

from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import User
from utils.decorators import authorize, get_req, post_req
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

@csrf_exempt
@authorize
@post_req
def set_socket_id(request, *args, **kwargs):
    try:
        body = json.loads(request.body)
        sid = body['sid']
        request.user.socket_id = sid
        request.user.save()

        return JsonResponse({
            'msg': "Success"
        })
    except Exception as e:
        print(e)

    
    return JsonResponse({
        'msg': "Invalid Data"
    }, status=400)

@csrf_exempt
@authorize
@post_req
def inactive(request, *args, **kwargs):
    try:
        body = json.loads(request.body)
        sid = body['sid']
        print(sid)
        if request.user.socket_id == sid:
            request.user.socket_id = None
            request.user.active = False
            request.user.save()

            return JsonResponse({
                'msg': "Success"
            })
    except Exception as e:
        print(e)

    return JsonResponse({
        'msg': "Invalid Data"
    }, status=400)