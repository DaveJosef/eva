from django.urls import path

from .views import HomePageView, EventDetailView, SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('signup/', SignUpView.as_view(), name='signup')
]
