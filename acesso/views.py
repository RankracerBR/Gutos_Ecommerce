from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from acesso.models import Comentario
from usuarios.models import Usuario
from acesso.forms import RegistroForm, UsuarioRegistroForm, ComentarioForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from acesso.models import RegistroToken, Comentario
from celery import shared_task
from django.urls import reverse
import random
import string


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
            return HttpResponse(
                'Verifique a caixa de entrada do seu email para confirmar'
            )
    else:
        form = RegistroForm()
    return render(request, 'enviar_token.html', {'form': form})

def verificacao(request, token):
    try:
        user = RegistroToken.objects.get(token=token)
        user.is_verified = True
        user.save()
        return redirect('acesso:cadastro', token=user.token)
    except RegistroToken.DoesNotExist:
        return HttpResponse(
            'Token inválido. Por favor, gere um novo token e tente novamente.'
        )

def cadastro(request, token):  
    if request.method == 'GET':
        try:
            registro_token = RegistroToken.objects.get(token=token)
        except RegistroToken.DoesNotExist:
            return redirect('acesso:verificacao')

        if registro_token.is_token_valid():
            form = UsuarioRegistroForm()
            return render(request, 'cadastro.html', {'form': form})
        else:
            return HttpResponse(
                'O token expirou. Por favor, gere um novo token.'
            )

    elif request.method == 'POST':
        form = UsuarioRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            registrar_cadastro.delay(usuario.id) 

            return redirect('acesso:pagina')
        else:
            return render(request, 'cadastro.html', {'form': form})


@shared_task
def registrar_cadastro(usuario_id):
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
        print(f"Nova conta adicionada com sucesso!: {usuario}")
    except Usuario.DoesNotExist:
        print("Erro ao registrar o cadastro")

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
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario_org = request.user
            comentario.save()
            registrar_operacao_comentario(comentario.id)

            return redirect('acesso:comentarios')
    else:
        form = ComentarioForm()
    comentarios = Comentario.objects.all()

    return render(request, 'comentarios.html', {'comentarios': comentarios, 
                                                'form': form})

@shared_task
def registrar_operacao_comentario(comentario_id):
    try:
        comentario = Comentario.objects.get(pk=comentario_id)
        print(f"Novo comentário salvo: {comentario}")
    except Comentario.DoesNotExist:
        print('Erro ao enviar comentário')

def assinatura(request):
    return render(request, 'assinatura.html')
