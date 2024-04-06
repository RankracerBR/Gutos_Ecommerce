from django.db import models


class RegistroToken(models.Model):
    nome = models.CharField(max_length=50, default='', blank=True)
    email = models.EmailField()

    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100, default='token')