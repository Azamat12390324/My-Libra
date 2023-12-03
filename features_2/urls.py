from django.urls import path
from features_2 import views


app_name = 'features_2'



urlpatterns = [
    path('features_2/', views.Features_2List.as_view(), name='features_2'),

]