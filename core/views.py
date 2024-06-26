from django.shortcuts import render,redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

#def index(request):
#    return redirect('/agenda/')
def login_user(request):
    return render(request, 'core/login.html')
def logout_user(request):
    logout(request)
    return redirect('/')
def submit_login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('/')
            else:
                messages.error(request, 'Usuario ou Senha Incorretos')

            return redirect('/')
    except:
        return render(request, 'core/login.html')
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos}
    return render(request, "core/agendamento.html", dados)