from django.http import JsonResponse

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