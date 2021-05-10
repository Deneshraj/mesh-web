from django.urls import path
from .views import *

urlpatterns = [
    path('', get_chats),
    path('add/', add_chat),
]