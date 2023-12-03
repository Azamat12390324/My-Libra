from django.shortcuts import render
from features_2.models import Features_2
from django.views.generic import ListView


class Features_2List(ListView):
    model = Features_2
    template_name = 'Features_2.html'
  

