from django.urls import path
from portfolio_image import views


app_name = 'portfolio_image'



urlpatterns = [
    path('portfolio_image/', views.Portfolio_imageList.as_view(), name='portfolio_image'),

]