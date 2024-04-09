from django.db import models

# Create your models here.

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100, default=None)
    valor_produto = models.FloatField()
    tipo_produto = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.nome_produto