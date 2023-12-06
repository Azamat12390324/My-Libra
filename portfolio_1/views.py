from django.shortcuts import render
from portfolio_1.models import Portfolio_1
from django.views.generic import ListView


class Portfolio_1List(ListView):
    model = Portfolio_1
    template_name = 'Portfolio_1.html'
  

