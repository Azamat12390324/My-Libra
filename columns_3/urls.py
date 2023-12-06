from django.urls import path
from columns_3 import views


app_name = 'columns_3'



urlpatterns = [
    path('columns_3/', views.Columns_3List.as_view(), name='columns_3'),

]