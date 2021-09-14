from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post

# def home(request):
#     return render(request, 'home.html', {})

class EventView(ListView):
    model = Post
    template_name = 'events.html'

def HomeView(request):

    return render(request, "home.html")