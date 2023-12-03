from django.urls import path
from home_8 import views

app_name = 'home_8'


urlpatterns = [
    path('home_8/', views.Home_8List.as_view(), name='home_8'),
        
]