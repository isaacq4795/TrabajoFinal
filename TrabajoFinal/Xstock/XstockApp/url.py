from django import views
from django.urls import path
from XstockApp.views import inicio,logear,Reguistar,Perfil,Informacion

urlpatterns = [
    path('',inicio),
    path('Login/',logear),
    path('Register',Reguistar),
    path('Profile',Perfil),
    path('About',Informacion),
]
