from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import EventView, HomeView, HeaderView, AboutView

urlpatterns = [
    path('', HomeView, name="home"),
    path('header/', HeaderView),
    path('about/', AboutView, name="about"),
    path('events/', EventView.as_view(), name="events"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

