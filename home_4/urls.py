from django.urls import path
from home_4 import views

app_name = 'home_4'


urlpatterns = [
    path('home_4/', views.Home_4List.as_view(), name='home_4'),
        
]