from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import Event
from usuarioevento.models import OuvinteEvento, PalestranteEvento


class HomePageView(ListView):
    model = Event
    template_name = 'home.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ouvintes'] = OuvinteEvento.objects.filter(
            evento=Event.objects.filter(pk=self.request.GET.get('evento'))[0])
        context['palestrantes'] = PalestranteEvento.objects.filter(
            evento=Event.objects.filter(pk=self.request.GET.get('evento'))[0])
        return context


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'event_create.html'
    context_object_name = 'events'


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'event_update.html'
    fields = ['nome', 'descricao', 'urlSite']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.autor != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'event_delete.html'
    context_object_name = 'events'


class MyEventsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'my_events.html'
    context_object_name = 'events'


@login_required(login_url='/accounts/login/')
def addEvento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Event.objects.get(id=id_evento)
    return render(request, 'event_create.html', dados)


@login_required(login_url='/accounts/login/')
def submitEvento(request):
    if request.POST:
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        urlSite = request.POST.get('urlSite')
        data = request.POST.get('data')
        hora = request.POST.get('hora')
        autor = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            Event.objects.filter(id=id_evento).update(nome=nome,
                                                      descricao=descricao,
                                                      urlSite=urlSite)
        else:
            Event.objects.create(nome=nome,
                                 descricao=descricao,
                                 urlSite=urlSite,
                                 data=data,
                                 hora=hora,
                                 autor=autor)
    return redirect('/')


@login_required(login_url='/accounts/login/')
def lista_eventos(request):
    autor = request.user
    evento = Event.objects.filter(autor=autor)
    dados = {'eventos': evento}
    return render(request, 'my_events.html', dados)


@login_required(login_url='/accounts/login/')
def delete_evento(request, id_evento):
    Event.objects.filter(id=id_evento).delete()
    return redirect('/')
