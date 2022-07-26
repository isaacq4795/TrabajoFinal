from django.contrib import admin

from XstockApp.models import Usuario
# Register your models here.

class Usuario_Admin(admin.ModelAdmin):

    datos = ('Nombre usuario', 'correo', 'contraseña')

admin.site.register(Usuario,Usuario_Admin)