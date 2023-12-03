from django.urls import path
from home_6 import views

app_name = 'home_6'


urlpatterns = [
    path('home_6/', views.Home_6List.as_view(), name='home_6'),
        
]