from django.urls import path, include
from assinantes import views

app_name = "assinantes"

urlpatterns = [
    path('pagina_assinante/', views.pagina_assinante, name="pagina_assinante")
]