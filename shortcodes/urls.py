from django.urls import path
from shortcodes import views

app_name = 'shortcodes'


urlpatterns = [
    path('alert_box/', views.Alert_boxList.as_view(), name='alert_box'),
    path('typography/', views.TypographyList.as_view(), name='typography'),
]