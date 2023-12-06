from django.shortcuts import render
from portfolio_2.models import Portfolio_2
from django.views.generic import ListView


class Portfolio_2List(ListView):
    model = Portfolio_2
    template_name = 'Portfolio_2.html'
  



