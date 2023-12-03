from django.shortcuts import render
from features_1.models import Features_1
from django.views.generic import ListView


class Features_1List(ListView):
    model = Features_1
    template_name = 'Features_1.html'
    


