from django.urls import path
from .views import *

urlpatterns = [
    path('friends', get_friends),
    path('socket', set_socket_id),
    path('inactive', inactive)
]   