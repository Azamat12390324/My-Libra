from django.shortcuts import render
from features_4.models import Features_4
from django.views.generic import ListView


class Features_4List(ListView):
    model = Features_4
    template_name = 'Features_4.html'
  
