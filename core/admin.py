from django.contrib import admin
from core.models import Evento

# Register your models here.
admin.tittle = "Gerenciamento de Agenda"

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','data_evento', 'data_criacao')
    list_filter = ('titulo', 'data_evento', )


admin.site.register(Evento, AgendaAdmin)