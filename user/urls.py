from django.urls import path
from .views import *

urlpatterns = [
    path('friends', get_friends),
]   