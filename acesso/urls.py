from django.urls import path
from acesso import views

app_name = "acesso"

urlpatterns = [
    path('', views.pagina, name="pagina"),
    path('verificacao/', views.verificacao_token, name="verificacao"),
    path('assinatura/', views.assinatura, name="assinatura"),
    path('verificacao/<str:token>/', views.verificacao, name="verificar"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('comentarios/', views.comentarios, name="comentarios"),
    path('logout', views.funcao_logout, name="logout"),
    path('login/', views.pagina_login, name="login")
]