from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import EventView, HomeView, HeaderView, AboutView

urlpatterns = [
    path('', HomeView, name="home"),
    path('header/', HeaderView),
    path('about/', AboutView, name="about"),
    path('events/', EventView.as_view(), name="events"),
] 

urlpatterns += staticfiles_urlpatterns()