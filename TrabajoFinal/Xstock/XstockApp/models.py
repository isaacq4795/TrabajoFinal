from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
# Create your models here.

class Usuario_registrofrom(UserCreationForm):

    nombre_usuario = forms.CharField(max_length=20)
    correo = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ['username', 'password1']

        help_texts = {k:"" for k in  fields}

class Usuario(models.Model):
    
    nombre_usuario = forms.CharField(max_length=20)
    correo = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)