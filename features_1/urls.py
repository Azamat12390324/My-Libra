from django.urls import path
from features_1 import views


app_name = 'features_1'



urlpatterns = [
    path('features_1/', views.Features_1List.as_view(), name='features_1'),

]