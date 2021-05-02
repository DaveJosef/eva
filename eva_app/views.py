from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import Event


class HomePageView(ListView):
    model = Event
    template_name = 'home.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'event_create.html'
    context_object_name = 'events'


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'event_update.html'
    context_object_name = 'events'


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'event_delete.html'
    context_object_name = 'events'


class MyEventsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'my_events.html'
    context_object_name = 'events'
