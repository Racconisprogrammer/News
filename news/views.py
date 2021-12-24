from django.shortcuts import render
from django.views.generic.list import ListView
from .models import HomeModelView

# Create your views here.


class HomePageView(ListView):
    model = HomeModelView
    template_name = 'home.html'