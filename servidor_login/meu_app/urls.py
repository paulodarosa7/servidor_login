from django.urls import path
from django.contrib.auth import login
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.autenticado, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.sair, name='logout'),



]