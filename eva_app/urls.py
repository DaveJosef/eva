from django.urls import path
from eva_app import views

from .views import HomePageView,\
    EventDetailView,\
    EventUpdateView,\
    MyEventsView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/addEvento/', views.addEvento),
    path('event/addEvento/submit', views.submitEvento),
    path('event/delete/<int:id_evento>/', views.delete_evento),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event_update'),
    path('myevents/', MyEventsView.as_view(), name='my_events'),
]
