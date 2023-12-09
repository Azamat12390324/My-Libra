from django.shortcuts import render
from .models import Testimonials, Faq, Error_404
from django.views.generic import ListView



class TestimonialsList(ListView):
    model = Testimonials
    paginate_by = 10
    template_name = 'Testimonials.html'
    
class FaqList(ListView):
    model = Faq
    paginate_by = 10
    template_name = 'Pages-faq.html'
    
class Error_404List(ListView):
    model = Error_404
    paginate_by = 10
    template_name = 'Error-404.html'
     
  

