from django.shortcuts import render
from .models import Home_3
from django.views.generic import ListView



class Home_3List(ListView):
    model = Home_3
    template_name = 'home_3.html'

  

