from django.urls import path
from .views import *

urlpatterns = [
    path('', login),
    path('signup', register),
    path('verify/<token>', verify_token),
    path('logout', logout),
    path('check_auth', check_auth),
]   