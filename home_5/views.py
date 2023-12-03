from django.shortcuts import render
from .models import Home_5
from django.views.generic import ListView



class Home_5List(ListView):
    model = Home_5
    paginate_by = 4
    template_name = 'home_5.html'

  

