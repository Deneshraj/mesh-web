import traceback

from django.http import JsonResponse
from utils.functions import verify_token

def post_req(function):
    def return_function(request, *args, **kwargs):
        try:           
            if request.method == 'POST':
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({ 'msg': "Invalid Method!" }, status=400)
        except Exception as e:
            print("Exception: ", e)
            return JsonResponse({ 'msg': "Server Error!" }, status=500)

    return return_function

def get_req(function):
    def return_function(request, *args, **kwargs):
        try:           
            if request.method == 'GET':
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({ 'msg': "Invalid Method!" }, status=400)
        except Exception as e:
            print("Exception: ", e)
            return JsonResponse({ 'msg': "Server Error!" }, status=500)

    return return_function

def put_req(function):
    def return_function(request, *args, **kwargs):
        try:           
            if request.method == 'PUT':
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({ 'msg': "Invalid Method!" }, status=400)
        except Exception as e:
            print("Exception: ", e)
            traceback.print_exc(e)
            return JsonResponse({ 'msg': "Internal Server Error!" }, status=500)

    return return_function

def authorize(function):
    def return_function(request, *args, **kwargs):
        try:
            auth_token = request.headers.get('authorization')
            if auth_token == None:
                return JsonResponse({ 'msg': "Unauthorized Request" }, status=400)
            else:
                token = auth_token.split(" ")
                if len(token) == 2 and token[0] == "Bearer":
                    isValid, user = verify_token(token[1])
                    if isValid:
                        request.user = user
                        return function(request, *args, **kwargs)
                    else:
                        return JsonResponse({ 'msg': "Unauthorized Request!" })
        except Exception as e:
            print("Exception: ", e)
            traceback.print_exc()
            return JsonResponse({ 'msg': "Server Error!" }, status=500)

    return return_function