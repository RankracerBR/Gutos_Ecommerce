from django.conf.urls.static import static
from django.urls import path
from acesso import views
from django.conf import settings

app_name = "acesso"

urlpatterns = [
    path('', views.pagina, name="pagina"),
    path('verificacao/', views.verificacao_token, name="verificacao"),
    path('assinatura/', views.assinatura, name="assinatura"),
    path('verificacao/<str:token>/', views.verificacao, name="verificar"),
    path('registro/<str:token>/', views.cadastro, name="cadastro"),
    path('comentarios/', views.comentarios, name="comentarios"),
    path('logout', views.funcao_logout, name="logout"),
    path('login/', views.pagina_login, name="login")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)