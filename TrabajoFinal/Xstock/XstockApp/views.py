from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from XstockApp.models import *


# Create your views here.


def inicio(request):

    return render(request, 'index.html')


def logear(request):

    if request.method == "post":
        form =  AuthenticationForm(request,data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username= usuario,password=contraseña)

            if user is not None:
                login(request,user)

                return render(request,"index.html")

            else:

                return render(request,"index.html")
        else:

            return render(request,"index.html")
    
    form = AuthenticationForm()


    return render(request,"Login.html",{'form': form})



def Reguistar(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save
            return render(request,"index.html")
    
    
    else:

        form = Usuario_registrofrom
    return render(request,"index.html",{"form":form})


    

def Perfil(request):
    
    return HttpResponse("Perfil")



def Informacion(request):
    
    return render(request,"About.html")



def home(request):

    return render(request,"index.html")