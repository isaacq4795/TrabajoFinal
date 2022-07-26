from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio,),
    path('Login/',logear),
    path('Register',Reguistar),
    path('Profile',Perfil),
    path('About',Informacion),
]
