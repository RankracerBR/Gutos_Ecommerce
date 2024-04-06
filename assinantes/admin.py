from django.contrib import admin
from .models import Assinante

@admin.register(Assinante)
class AdminAssinantes(admin.ModelAdmin):
    list_display = ('assinante', 'tipo_assinante', 'valor_assinatura')
    list_filter = ('assinante', 'tipo_assinante', 'valor_assinatura')