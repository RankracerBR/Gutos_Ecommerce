from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto, CategoriaProduto
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Carrinho, ItemCarrinho
from django.contrib.auth.decorators import login_required

# Create your views here.

def pagina_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'pagina_produtos.html', {'produtos':produtos})

@login_required(login_url='acesso:login')
def adicionar_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)

    if ItemCarrinho.objects.filter(produto=produto, carrinho=carrinho).exists():
        item = ItemCarrinho.objects.get(produto=produto, carrinho=carrinho)
        item.quantidade += 1
        item.save()
    else:
        item = ItemCarrinho.objects.create(produto=produto, quantidade=1)
        carrinho.itens.add(item)

    return redirect('produtos:carrinho')

@login_required(login_url='acesso:login')
def ver_carrinho(request):
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    itens = carrinho.itens.all()

    total = sum(item.produto.valor_produto * item.quantidade for item in itens)

    return render(request, 'carrinho.html', {'carrinho': carrinho, 'itens': itens, 'total': total})

@login_required(login_url='acesso:login')
def finalizar_compra(request):
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    carrinho.itens.clear()
    return render(request, 'compra_finalizada.html')