from django.shortcuts import render
from portfolio_3.models import Portfolio_3
from django.views.generic import ListView


class Portfolio_3List(ListView):
    model = Portfolio_3
    template_name = 'Portfolio_3.html'
  
