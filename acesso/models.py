from django.db import models
from usuarios.models import Usuario
from django.utils import timezone

class RegistroToken(models.Model):
    nome = models.CharField(max_length=50, default='', blank=True)
    email = models.EmailField()

    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100, default='token')
    token_criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token
    
    def is_token_valid(self):
        tempo_expiracao = timezone.timedelta(minutes=5)
        tempo_atual = timezone.now()

        return (tempo_atual - self.token_criado) < tempo_expiracao

class Comentario(models.Model):
    usuario_org = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentarios = models.TextField()
    
    def __str__(self):
        return f"{self.usuario_org}, {self.comentarios}"