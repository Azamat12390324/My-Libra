from django.urls import path
from features_3 import views


app_name = 'features_3'



urlpatterns = [
    path('features_3/', views.Features_3List.as_view(), name='features_3'),

]