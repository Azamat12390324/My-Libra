from django.shortcuts import render
from .models import Home_8
from django.views.generic import ListView



class Home_8List(ListView):
    model = Home_8
    paginate_by = 10
    template_name = 'home_8.html'

 


