from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import EventView, HomeView, HeaderView, AboutView, EventDetailView

urlpatterns = [
    path('', HomeView, name="home"),
    path('header/', HeaderView),
    path('about/', AboutView, name="about"),
    path('events/', EventView.as_view(), name="events"),
    path('event/<int:pk>', EventDetailView.as_view(), name="event_details" )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# <int:pk>