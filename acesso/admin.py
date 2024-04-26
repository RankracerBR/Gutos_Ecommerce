from django.contrib import admin
from .models import Comentario

# Register your models here.

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario_org', 'comentarios')
    list_filter = ('usuario_org', 'comentarios')