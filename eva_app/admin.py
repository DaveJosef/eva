from django.contrib import admin
from .models import Event


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'dataHora')
    list_filter = ('autor', 'dataHora')

admin.site.register(Event, EventoAdmin)
