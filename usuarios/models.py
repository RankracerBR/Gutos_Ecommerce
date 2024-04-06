from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=40, default='nome_completo')
    idade = models.PositiveSmallIntegerField()
    email = models.EmailField()
    senha = models.TextField(max_length=150, verbose_name="Senha")
    imagem = models.ImageField(upload_to='imgs/')

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100, default=None)
    valor_produto = models.FloatField()
    tipo_produto = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.nome_produto