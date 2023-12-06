from django.shortcuts import render
from columns_2.models import Columns_2
from django.views.generic import ListView


class Columns_2List(ListView):
    model = Columns_2
    template_name = 'Portfolio_2_columns.html'
  


