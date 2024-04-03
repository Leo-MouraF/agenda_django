from core.models import Evento
from django.contrib import admin


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento', )


admin.site.register(Evento, EventoAdmin)
