from django.urls import path
from portfolio_2 import views


app_name = 'portfolio_2'



urlpatterns = [
    path('portfolio_2/', views.Portfolio_2List.as_view(), name='portfolio_2'),

]