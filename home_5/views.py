from django.shortcuts import render
from .models import Home_5
from django.views.generic import ListView


def home_5(request):
    home_5 = Home_5.objects.all()
    context ={'home5': home_5}
    paginate_by = 4
    return render(request, 'home_5.html',context)


#class Home_5List(ListView):
    #model = Home_5
    #paginate_by = 4
    #template_name = 'home_5.html'

  

