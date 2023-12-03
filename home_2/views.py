from django.shortcuts import render
from home_2.models import Home_2
from django.views.generic import ListView







class Home_2List(ListView):
    model = Home_2
    template_name = 'home_2.html'
  
