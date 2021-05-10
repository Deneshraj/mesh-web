import json

from django.shortcuts import render
from django.db.models import Q
from utils.decorators import *
from utils.functions import *
from django.views.decorators.csrf import csrf_exempt
from .models import Chat

# Create your views here.
@csrf_exempt
@authorize
@post_req
def get_chats(request, *args, **kwargs):
    if(request.body != ""):
        body = json.loads(request.body)
        to_user = body.get('to_user')
        if(is_valid_uuid(to_user)):
            to_user = User.objects.filter(id=uuid.UUID(to_user))
            if len(to_user) > 0:
                to_user = to_user.first()
                chats = Chat.objects.filter(Q(from_user=request.user, to_user=to_user) | Q(to_user=request.user, from_user=to_user)).order_by('date_created')
                chat_return = []
                for chat in chats:
                    chat_return.append(chat.to_dict())

                return JsonResponse({ 'chats': chat_return })

    return JsonResponse({ 'msg': "Invalid Data" })

@csrf_exempt
@authorize
@post_req
def add_chat(request, *args, **kwargs):
    try:
        body = json.loads(request.body)
        
        from_user = request.user
        to_user = get_user_from_id(body.get('to_user'))
        message = body.get("message")

        if from_user != None and to_user != None:
            chat = Chat(message=message, from_user=from_user, to_user=to_user)
            chat.save()
            return JsonResponse({ 'chat': chat.to_dict() })
        
        return JsonResponse({'msg': "Invalid Data"}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({
            'msg': "Invalid Data"
        }, status=400)