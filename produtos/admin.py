from .models import Produto, CategoriaProduto, ItemCarrinho, Carrinho
from django.contrib import admin


# Register your models here.

@admin.register(CategoriaProduto)
class CategoriaProdutoAdmin(admin.ModelAdmin):
    list_display = ('categoria',)
    list_filter = ('categoria',)


@admin.register(Produto)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'valor_produto','tipo_produto','foto_produto')
    list_filter = ('nome_produto', 'valor_produto','tipo_produto','foto_produto')

@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario_orgm', 'produto', 'quantidade')
    list_filter = ('usuario_orgm', 'produto', 'quantidade')

@admin.register(Carrinho)
class Carrinho(admin.ModelAdmin):
    list_display = ('usuario', 'criado_em')
    list_filter = ('usuario', 'criado_em')