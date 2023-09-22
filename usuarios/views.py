from django.contrib.messages import constants
from django.contrib import messages
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request,'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        telefone_fixo = request.POST.get('telefone_fixo')
        telefone = request.POST.get('telefone')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not(senha == confirmar_senha):
            messages.add_message(request, constants.INFO, 'Senhas Diferentes!!')
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(request, constants.INFO, 'Você já tem uma conta cadastrada!')
            return redirect(reverse('cadastro'))
        
        user = User.objects.create_user(username=username,email=email,senha=senha,password=senha)
        user.save()
        messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso!')
        return redirect(reverse('login'))

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = username.POST.get('username')
        senha = senha.POST.get('senha')
        
        
        user = auth.authenticate(username=username,password=senha)
        
        
        if not user:
            messages.add_message(request, constants.ERROR, 'Usuario não existe!')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect('eventos/novo_evento/')