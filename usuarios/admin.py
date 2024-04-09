from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from django.contrib import admin
from acesso.forms import UsuarioRegistroForm
from django.conf import settings
from django.contrib import messages
import psycopg2

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioRegistroForm
    list_display = ('username', 'email', 'imagem')
    list_filter =  ('username', 'email', 'imagem')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 
                                             'imagem')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 
                                   'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )