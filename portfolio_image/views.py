from django.shortcuts import render
from portfolio_image.models import Portfolio_image
from django.views.generic import ListView


class Portfolio_imageList(ListView):
    model = Portfolio_image
    template_name = 'portfolio-big-image.html'
  


