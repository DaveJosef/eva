from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from .models import OuvinteEvento, PalestranteEvento
from eva_app.models import Event


class OuvinteEventoCreateView(LoginRequiredMixin, CreateView):
    model = OuvinteEvento
    template_name = 'inscricao_create.html'
    fields = []
    success_url = reverse_lazy('my_events')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.evento = Event.objects.filter(
            pk=self.request.GET.get('evento'))[0]
        return super().form_valid(form)


class PalestranteEventoCreateView(LoginRequiredMixin, CreateView):
    model = PalestranteEvento
    template_name = 'palestra_create.html'
    fields = ['evento']
    success_url = reverse_lazy('my_events')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class OuvinteEventoDeleteView(LoginRequiredMixin, DeleteView):
    model = OuvinteEvento
    template_name = 'inscricao_delete.html'
    success_url = reverse_lazy('home')


class PalestranteEventoDeleteView(LoginRequiredMixin, DeleteView):
    model = PalestranteEvento
    template_name = 'palestra_delete.html'
    success_url = reverse_lazy('home')
