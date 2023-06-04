from .views import *
from django.urls import path

urlpatterns = [
    path('login/',login),
    path('login-validation/',loginValidation),
    path('signup/',signup),
    path('save-user/',saveUser),
    path('home/',home),
    path('logout/',logout),
    path('delete/',delete),
    path('send/',send),
    path('deletecdb/',deleteConversation),
]