from django.urls import path
from contact import views


app_name = 'contact'



urlpatterns = [
    path('contact/', views.ContactList.as_view(), name='contact'),

]