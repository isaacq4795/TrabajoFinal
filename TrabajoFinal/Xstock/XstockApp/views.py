from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from XstockApp.models import *


# Create your views here.


def inicio(request):

    inicia = loader.get_template('')

    pag_inicial = inicia.render()

    return HttpResponse(pag_inicial)


def logear(request):

    if request.method == "post":
        form =  AuthenticationForm(request,data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username= usuario,password=contraseña)

            if user is not None:
                login(request,user)

                return render(request,"XstockApp/index.html")

            else:

                return render(request,"XstockApp/index.html")
        else:

            return render(request,"XstockApp/index.html")
    
    form = AuthenticationForm()


    return render(request,"XstockApp/Login.html",{'form': form})

def Reguistar(request):
    if request.method == "post":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save
            return render(request,"XstockApp/index.html")
    
    
    else:

        form = Usuario_registrofrom
    return render(request,"XstockApp/index.html",{"form":form})


    

def Perfil(request):
    
    return HttpResponse("Perfil")

def Informacion(request):
    
    return HttpResponse("Info sobre mi")

def home(request):

    return HttpResponse("inicio pagina")