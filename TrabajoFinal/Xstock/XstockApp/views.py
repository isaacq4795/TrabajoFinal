from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def inicio(request):

    inicia = loader.get_template('')

    pag_inicial = inicia.render()

    return HttpResponse(pag_inicial)


def logear(request):
    
    return render(request,"XstockApp/index.html",{})

def Reguistar(request):
    
    return HttpResponse("Registro")

def Perfil(request):
    
    return HttpResponse("Perfil")

def Informacion(request):
    
    return HttpResponse("Info sobre mi")

def home(request):

    return HttpResponse("inicio pagina")