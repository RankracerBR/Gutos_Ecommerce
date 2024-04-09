from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 , get_list_or_404
from django.urls import reverse_lazy
from .models import Usuario


# Create your views here.

def pagina_usuarios(request):
    return render(request, 'usuarios.html')

@login_required(login_url='acesso:login')
def pagina_conta(request):
    return render(request, 'pagina_conta.html')

def acesso_extrato(request):
    ...

def adicionar_colegas(request):
    ...