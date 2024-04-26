from django.shortcuts import render

# Create your views here.

def pagina_assinante(request):
    return render(request, 'pagina_assinante.html')

def produtos_exclusivos(request):
    ...
