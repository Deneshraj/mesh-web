from django.urls import path, include

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('user/', include('user.urls')),
    path('chats/', include('chats.urls')),
]   