from django.urls import path
from home_5 import views

app_name = 'home_5'


urlpatterns = [
    path('home_5/', views.Home_5List.as_view(), name='home_5'),
        
]