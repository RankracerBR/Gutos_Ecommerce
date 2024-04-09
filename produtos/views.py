from django.shortcuts import render

# Create your views here.

def pagina_produtos(request):
    return render(request, 'pagina_produtos.html')