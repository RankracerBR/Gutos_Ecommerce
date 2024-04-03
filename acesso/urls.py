from django.urls import path
from acesso import views

urlpatterns = [
    path('', views.pagina, name="pagina"),
]