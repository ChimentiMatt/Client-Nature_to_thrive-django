from django.urls import path
# from . import views
from .views import EventView, HomeView, HeaderView, AboutView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView, name="home"),
    path('header/', HeaderView),
    path('about/', AboutView, name="about"),
    path('events/', EventView.as_view(), name="events"),
]
