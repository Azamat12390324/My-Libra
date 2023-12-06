from django.urls import path
from home_5 import views

app_name = 'home_5'


urlpatterns = [
    path('home_5/', views.home_5, name='home_5'),
        
]