from django.urls import path
from home_2 import views


app_name = 'home_2'



urlpatterns = [
    path('home_2/', views.Home_2List.as_view(), name='home_2'),

]