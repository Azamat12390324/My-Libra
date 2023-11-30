from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_1.urls')),
    path('', include('home_2.urls')),
    path('', include('home_3.urls')),
    path('', include('home_4.urls')),
    path('', include('home_5.urls')),
    path('', include('home_6.urls')),
    path('', include('home_7.urls')),
    path('',include('home_8.urls')),
    
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


