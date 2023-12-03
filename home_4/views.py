from django.shortcuts import render
from .models import Home_4
from django.views.generic import ListView



class Home_4List(ListView):
    model = Home_4
    template_name = 'home_4.html'

  

