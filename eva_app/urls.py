from django.urls import path

from .views import HomePageView,\
    EventDetailView,\
    EventCreateView,\
    EventUpdateView,\
    EventDeleteView,\
    MyEventsView,\
    SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/new/', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('myevents/', MyEventsView.as_view(), name='my_events'),
    path('signup/', SignUpView.as_view(), name='signup')
]
