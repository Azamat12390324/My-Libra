from django.urls import path
from portfolio_3 import views


app_name = 'portfolio_3'



urlpatterns = [
    path('portfolio_3/', views.Portfolio_3List.as_view(), name='portfolio_3'),

]