from django.urls import path
from home_7 import views

app_name = 'home_7'


urlpatterns = [
    path('home_7/', views.Home_7List.as_view(), name='home_7'),
        
]