from django.shortcuts import render
from .models import Alert_box, Typography
from django.views.generic import ListView


class Alert_boxList(ListView):
    model = Alert_box
    paginate_by = 10
    template_name = 'Shortcodes-alert-box.html'
    
class TypographyList(ListView):
    model = Typography
    paginate_by = 10
    template_name = 'Shortcodes-typography.html'
    





#def alert_box(request):
    # =Alert_box .objects.all()
    #context ={'alert_box': alert_box}
    #Epaginate_by = 4
    #return render(request, 'Shortcodes-alert-box.html',context)

    
#def typography(request):
    #typography = Typography.objects.all()
    #context ={'typography': typography}
    #paginate_by = 4
    #eturn render(request, 'Shortcodes-typography.html',context)


    
     

