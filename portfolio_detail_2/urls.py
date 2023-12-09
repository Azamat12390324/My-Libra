from django.urls import path
from portfolio_detail_2 import views


app_name = 'portfolio_detail_2'



urlpatterns = [
    path('portfolio_detail_2/', views.Portfolio_detail_2List.as_view(), name='portfolio_detail_2'),

]