from django.shortcuts import render
from features_3.models import Features_3
from django.views.generic import ListView


class Features_3List(ListView):
    model = Features_3
    template_name = 'Features_3.html'
  


