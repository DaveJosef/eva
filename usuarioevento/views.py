from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import OuvinteEvento, PalestranteEvento


class OuvinteEventoCreateView(LoginRequiredMixin, CreateView):
    model = OuvinteEvento
    template_name = 'inscricao_create.html'
    context_object_name = 'inscricoes'
    fields = '__all__'


class PalestranteEventoCreateView(LoginRequiredMixin, CreateView):
    model = PalestranteEvento
    template_name = 'palestra_create.html'
    context_object_name = 'palestras'
    fields = '__all__'

