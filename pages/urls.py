from django.urls import path
from pages import views

app_name = 'pages'


urlpatterns = [
    path('testimonials/', views.TestimonialsList.as_view(), name='testimonials'),
    path('faq/', views.FaqList.as_view(), name='faq'),
    path('error_404/', views.Error_404List.as_view(), name='error_404'),
]