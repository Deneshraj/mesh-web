import hashlib
import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from utils.decorators import post_req
from .models import User

# Create your views here.
@csrf_exempt
@post_req
def login(request, *args, **kwargs):
        try:
            post_data = json.loads(request.body)
            email = post_data["email"]
            password = post_data["password"]
            password = hashlib.sha256(password.encode()).hexdigest()

            user = User.objects.filter(email=email)
            isUserExist = user.exists()
            if not isUserExist:
                return JsonResponse({ 'msg': "User Doesn't Exist" }, status=404)
            
            if user[0].password == password:
                return JsonResponse({ 'msg': "Welcome to Mesh" }, status=200)
            else:
                return JsonResponse({ 'msg': "Invalid Password!" })
        except KeyError:
            return JsonResponse({ 'msg': "Please provide all the fields" }, status=400)

@csrf_exempt
@post_req
def register(request, *args, **kwargs):
    try:
        post_data = json.loads(request.body)
        email = post_data["email"]
        password = post_data["password"]
        password = hashlib.sha256(password.encode()).hexdigest()

        user = User(email=email, password=password)
        user.save()

        return JsonResponse({ 'msg': "Welcome to Mesh" })
    except KeyError:
        return JsonResponse({ 'msg': "Please provide all the fields" }, status=400)