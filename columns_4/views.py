from django.shortcuts import render
from columns_4.models import Columns_4
from django.views.generic import ListView


class Columns_4List(ListView):
    model = Columns_4
    template_name = 'portfolio-4-columns.html'
  


