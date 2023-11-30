from django.shortcuts import render
from home_1.models import Home_1
from django.views.generic import ListView







class Home_1List(ListView):
    model = Home_1
    template_name = 'home_1.html'
    


