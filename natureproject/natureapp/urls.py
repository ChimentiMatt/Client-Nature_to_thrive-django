from django.urls import path
# from . import views
from .views import EventView, HomeView, HeaderView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView),
    path('header/', HeaderView),
    path('events/', EventView.as_view(), name="home"),
]
