from django.shortcuts import render
from .models import Home_7
from django.views.generic import ListView



class Home_7List(ListView):
    model = Home_7
    paginate_by = 10
    template_name = 'home_7.html'

  


