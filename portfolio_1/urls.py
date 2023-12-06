from django.urls import path
from portfolio_1 import views


app_name = 'portfolio_1'



urlpatterns = [
    path('portfolio_1/', views.Portfolio_1List.as_view(), name='portfolio_1'),

]