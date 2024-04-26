from django.db import models
from django.utils import timezone
from usuarios.models import Usuario

# Create your models here.

class CategoriaProduto(models.Model):
    categoria = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.categoria


class Produto(models.Model):
    nome_produto = models.CharField(max_length=200, default=None)
    valor_produto = models.FloatField()
    tipo_produto = models.ForeignKey(CategoriaProduto, on_delete=models.CASCADE)
    foto_produto = models.ImageField(upload_to='produtos/', default=True)

    def __str__(self):  
        return f"{self.nome_produto} {self.valor_produto}"


class ItemCarrinho(models.Model):
    usuario_orgm = models.OneToOneField(Usuario, default=True ,on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome_produto}'


class Carrinho(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    itens = models.ManyToManyField(ItemCarrinho, blank=True)
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'