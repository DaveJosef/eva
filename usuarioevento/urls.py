from django.urls import path

from .views import (
    OuvinteEventoCreateView,
    PalestranteEventoCreateView,
    OuvinteEventoDeleteView,
    PalestranteEventoDeleteView
)

urlpatterns = [
    path('inscricao/new/', OuvinteEventoCreateView.as_view(),
         name='ouvinteevento_create'),
    path('palestra/new/', PalestranteEventoCreateView.as_view(),
         name='palestranteevento_create'),
    path('inscricao/<int:pk>/delete/',
         OuvinteEventoDeleteView.as_view(), name='ouvinteevento_delete'),
    path('palestra/<int:pk>/delete/', PalestranteEventoDeleteView.as_view(),
         name='palestranteevento_delete')
]
