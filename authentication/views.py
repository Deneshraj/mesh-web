import hashlib
import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from utils.decorators import *
from user.models import User
from .models import *
from utils.functions import is_valid_uuid

# Create your views here.
@csrf_exempt
@post_req
def login(request, *args, **kwargs):
    post_data = json.loads(request.body)
    email = post_data.get("email")
    password = post_data.get("password")

    if (email == None) or (password == None):
        return JsonResponse({ 'msg': "Please provide all the fields" }, status=400)

    password = hashlib.sha256(password.encode()).hexdigest()

    users = User.objects.filter(email=email)
    isUserExist = users.exists()

    if not isUserExist:
        return JsonResponse({ 'msg': "User Doesn't Exist" }, status=404)
    user = users[0]
    if user.password == password:
        tokens = AuthToken.objects.filter(user=user)
        if len(tokens) > 0:
            for token in tokens:
                token.delete()
        
        token = AuthToken(user=user)
        token.save()

        return JsonResponse({ 'msg': "Welcome to Mesh", 'token': token.to_dict() }, status=200)
    else:
        return JsonResponse({ 'msg': "Invalid Password!" })

@csrf_exempt
@post_req
def register(request, *args, **kwargs):
    post_data = json.loads(request.body)
    email = post_data.get("email")
    password = post_data.get("password")

    if (email == None) or (password == None):
        return JsonResponse({ 'msg': "Please provide all the fields" }, status=400)

    password = hashlib.sha256(password.encode()).hexdigest()
    user = User(email=email, password=password)
    user.save()
    verify_token = VerifyToken(user=user)
    verify_token = verify_token.save()

    return JsonResponse({ 'msg': "Welcome to Mesh, Please verify your account sent to your Email" })

@csrf_exempt
@get_req
def verify_token(request, *args, **kwargs):
    token = kwargs.get('token')
    if is_valid_uuid(token):
        vtokens = VerifyToken.objects.filter(verify_token=token)
        if len(vtokens) >= 1:
            vtoken = vtokens.first()
            user = vtoken.user
            user.verified = True
            user.save()
            vtoken.delete()
            return HttpResponse('<h1>Verified</h1>', content_type="text/html")

    return JsonResponse({ 'msg': "Invalid Token!" }, status=400)

@csrf_exempt
@authorize
@put_req
def logout(request, *args, **kwargs):
    msg = str(request.body.decode())

    if msg == "logout":
        token = request.headers.get('authorization').split(" ")[1]

        if is_valid_uuid(token):
            auth_token = AuthToken.objects.filter(auth_token=token).first()
            if auth_token != None:
                auth_token.delete()
        
        return JsonResponse({"msg": "Logged  out!", "logged_out": True})
    else:
        return JsonResponse({"msg": "Invalid Request!"}, status=400)

@csrf_exempt
@authorize
@get_req
def check_auth(request, *args, **kwargs):
    token = request.headers.get('authorization').split(" ")[1]
    if is_valid_uuid(token):
        auth_token = AuthToken.objects.filter(auth_token=token).first()
        return JsonResponse({"auth": auth_token != None})

    return JsonResponse({"auth": False})