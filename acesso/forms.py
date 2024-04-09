from django.contrib.auth.forms import UserCreationForm
from django import forms
from acesso.models import RegistroToken
from usuarios.models import Usuario


class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroToken
        fields = ('nome','email')
        labels = {
            'nome': 'Nome'
        }

class UsuarioRegistroForm(UserCreationForm):
    idade = forms.IntegerField(initial=0)

    class Meta:
        model = Usuario
        fields = ['username', 'idade', 'email', 'imagem']