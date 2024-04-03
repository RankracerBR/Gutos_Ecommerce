from usuarios.models import Usuario
from django.db import models

# Create your models here.

class Assinante(models.Model):
    assinante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_assinante = models.CharField(max_length=50, default=None)
    valor_assinatura = models.FloatField()
