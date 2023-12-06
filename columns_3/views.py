from django.shortcuts import render
from columns_3.models import Columns_3
from django.views.generic import ListView


class Columns_3List(ListView):
    model = Columns_3
    template_name = 'portfolio-3-columns.html'
  
