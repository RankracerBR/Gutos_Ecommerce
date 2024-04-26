from django.conf.urls.static import static
from django.urls import path
from produtos import views
from django.conf import settings

app_name = 'produtos'

urlpatterns = [
    path('pagina_produtos/', views.pagina_produtos, name="pagina_produtos"),
    path('adicionar-carrinho/<int:produto_id>/', views.adicionar_carrinho, 
                                                 name='adicionar_carrinho'),
    path('carrinho/', views.ver_carrinho, name='carrinho'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)