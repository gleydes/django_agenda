from django.shortcuts import render,redirect
from core.models import Evento
# Create your views here.

#def index(request):
#    return redirect('/agenda/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos}
    return render(request, "core/agendamento.html", dados)