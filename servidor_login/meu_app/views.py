from django.shortcuts import render,redirect,get_object_or_404
from .models import Usuario
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def welcome(request):
    return render(request, 'home.html')


def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirme_senha = request.POST.get('confirme_senha')
        
        if senha == confirme_senha:
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.first_name = nome
            user.save()
            return redirect('login')
        else:
            return render(request, 'cadastro.html', {'error': 'As senhas não coincidem.'})
    return render(request, 'cadastro.html')


def autenticado(request):
    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = authenticate(request, username=username, password=senha)

        if usuario is not None:
            auth_login(request, usuario)
            return redirect('/inicio')  # redireciona para /viagem apos login  # <- esta é a forma correta
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos.'})

    return render(request, 'login.html')


@login_required(login_url='login')
def inicio(request):
    return render(request, 'inicio.html')

def sair(request):
    logout(request)
    return redirect('welcome')

