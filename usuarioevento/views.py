from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import OuvinteEvento, PalestranteEvento


class OuvinteEventoCreateView(LoginRequiredMixin, CreateView):
    model = OuvinteEvento
    template_name = 'inscricao_create.html'
    fields = ['evento']
    success_url = reverse_lazy('my_events')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class PalestranteEventoCreateView(LoginRequiredMixin, CreateView):
    model = PalestranteEvento
    template_name = 'palestra_create.html'
    fields = ['evento']
    success_url = reverse_lazy('my_events')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
