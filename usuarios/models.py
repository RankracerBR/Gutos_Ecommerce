from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Usuario(AbstractUser):
    idade = models.PositiveSmallIntegerField(default=0)
    imagem = models.ImageField(upload_to='imgs/')
