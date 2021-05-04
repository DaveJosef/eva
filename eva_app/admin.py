from django.contrib import admin
from .models import Event


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data', 'hora')
    list_filter = ('autor', 'data', 'hora')


admin.site.register(Event, EventoAdmin)
