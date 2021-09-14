from django.urls import path
# from . import views
from .views import EventView, HomeView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView),
    path('events/', EventView.as_view(), name="home")
]
