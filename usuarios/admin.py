from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class AdminUsuario(admin.ModelAdmin):
    list_display = ('nome', 'email','imagem')
    list_filter = ('nome', 'email', 'imagem')

