from django.urls import path
from features_4 import views


app_name = 'features_4'



urlpatterns = [
    path('features_4/', views.Features_4List.as_view(), name='features_4'),

]