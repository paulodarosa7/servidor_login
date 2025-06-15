from django.shortcuts import render,redirect,get_object_or_404
from .models import Usuario
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# pagina inicial da aplicacao
def welcome(request): 
    return render(request, 'home.html')


def cadastro(request): #realiza o cadastro do user, por meio do metodo post
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirme_senha = request.POST.get('confirme_senha')
        
        if senha == confirme_senha: # confirmação basica de senha
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.first_name = nome
            user.save()
            return redirect('login')
        else: # senha não confere
            return render(request, 'cadastro.html', {'error': 'As senhas não coincidem.'})
    return render(request, 'cadastro.html')


def autenticado(request): #funçao de autenticacao (login) do usuario, login
    if request.method == "POST": #desenvolvimento do metodo post para o funcionamento do login e senha
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = authenticate(request, username=username, password=senha) #realiza a autenticaçao do usuario a partir do username e senha

        if usuario is not None:
            auth_login(request, usuario)
            return redirect('/inicio')  # redireciona para /inicio apos login
        
        else: # autenticaçao falhou
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos.'})

    return render(request, 'login.html')


@login_required(login_url='login') #so deve ser acessado apos realizado ologin
def inicio(request):
    return render(request, 'inicio.html')

#logout do usuario, retornando para a tela inicial
def sair(request): #esta opção so existe dentro de /inicio
    logout(request)
    return redirect('welcome')

