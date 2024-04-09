from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from usuarios.models import Usuario
from acesso.forms import RegistroForm, UsuarioRegistroForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from acesso.models import RegistroToken
import random

# Create your views here.

def pagina(request):
    return render(request, 'acesso.html')

def verificacao_token(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_verified = False
            user.token = str(random.random()).split('.')[1]
            user.save()

            domain_name = get_current_site(request).domain
            link = f'http://{domain_name}/verificacao/{user.token}'
            send_mail(
                'Verificação de Email',
                f'Clique para completar seu cadastro: {link}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            return HttpResponse('Verifique a caixa de entrada do seu email para confirmar')
    else:
        form = RegistroForm()
    return render(request, 'enviar_token.html', {'form': form})

def verificacao(request, token):
    try:
        user = RegistroToken.objects.get(token=token)
        user.is_verified = True
        user.save()
        return redirect('acesso:cadastro')
    except RegistroToken.DoesNotExist:
        return render(request, 'cadastro.html')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            login(request,usuario)
            return redirect('acesso:pagina')
    else:
        form = UsuarioRegistroForm()

    return render(request, 'cadastro.html', {'form': form})

def pagina_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('usuarios:pagina_conta')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def funcao_logout(request):
    logout(request)
    return redirect('acesso:pagina')

def comentarios(request):
    return render(request, 'comentarios.html')

def assinatura(request):
    return render(request, 'assinatura.html')
