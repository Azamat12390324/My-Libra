from django.urls import path
from columns_4 import views


app_name = 'columns_4'



urlpatterns = [
    path('columns_4/', views.Columns_4List.as_view(), name='columns_4'),

]