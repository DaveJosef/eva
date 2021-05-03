from django.urls import path

from .views import OuvinteEventoCreateView, PalestranteEventoCreateView

urlpatterns = [
    path('inscricao/new/', OuvinteEventoCreateView.as_view(), name='ouvinteevento_create'),
    path('palestra/new/', PalestranteEventoCreateView.as_view(), name='palestranteevento_create')
]
