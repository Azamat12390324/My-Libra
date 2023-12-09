from django.shortcuts import render
from portfolio_detail_2.models import Portfolio_detail_2
from django.views.generic import ListView


class Portfolio_detail_2List(ListView):
    model = Portfolio_detail_2
    template_name = 'Portfolio-project-detail-2.html'
                                                    

