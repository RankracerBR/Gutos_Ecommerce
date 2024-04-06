from django import forms
from acesso.models import RegistroToken

class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroToken
        fields = ('nome','email')
        labels = {
            'nome': 'Nome'
        }