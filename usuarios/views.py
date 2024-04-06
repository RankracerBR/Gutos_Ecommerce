from django.shortcuts import render

# Create your views here.

def pagina_usuarios(request):
    return render(request, 'usuarios.html')

def pagina_conta(request):
    return render(request, 'pagina_conta.html')

def acesso_extrato(request):
    ...

def adicionar_colegas(request):
    ...