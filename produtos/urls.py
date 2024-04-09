from django.urls import path
from produtos import views

app_name = 'produtos'

urlpatterns = [
    path('pagina_produtos/', views.pagina_produtos, name="pagina_produtos")
]