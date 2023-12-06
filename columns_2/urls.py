from django.urls import path
from columns_2 import views


app_name = 'columns_2'



urlpatterns = [
    path('columns_2/', views.Columns_2List.as_view(), name='columns_2'),

]