from django.shortcuts import render
from .models import Home_6
from django.views.generic import ListView



class Home_6List(ListView):
    model = Home_6
    paginate_by = 4
    template_name = 'home_6.html'

  

