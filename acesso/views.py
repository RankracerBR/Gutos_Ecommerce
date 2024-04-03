from django.shortcuts import render

# Create your views here.

def pagina(request):
    return render(request, 'acesso.html')

def enviar_token(request):
    ...

def criar_conta(request):
    ...

def comentarios(request):
    ...
