from django.urls import path
from home_3 import views

app_name = 'home_3'


urlpatterns = [
    path('home_3/', views.Home_3List.as_view(), name='home_3'),
        
]