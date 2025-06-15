# Projeto de Autenticação em Django (cadastro, login e logout)!

Este é um projeto simples de autenticação com cadastro, login e logout usando Django. Utilizaremos a linguagem de programação Python e algumas bibliotecas e também como banco de dados será implementado o SQLite

---

## Configuração do Ambiente

Recomenda-se usar um ambiente virtual para isolar as dependências do projeto.

### Criar ambiente virtual (OBS: Evite colocar o Django dentro da pasta do ambiente virtual, deve ser feito em pastas separadas!!!!!!!!!!!

```bash
virtualenv ambiente_virtual
```

### Ativação do ambiente virtual
```bash
source ambiente_virtual/bin/activate
```
### Instalar dependências Django
```bash
pip3 install django django-admin
```
### Entre no diretório servidor_login
```bash
cd ~/--caminho--/servidor_login
```
### Upar o servidor na Web
```bash
 python3 manage.py makemigrations
 python3 manage.py migrate
 python3 manage.py runserver
```






