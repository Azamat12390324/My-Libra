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
    path('',include('features_1.urls')),
    path('',include('features_2.urls')),
    path('',include('features_3.urls')),
    path('',include('features_4.urls')),
    path('',include('portfolio_1.urls')),
    path('',include('portfolio_2.urls')),
    path('',include('portfolio_3.urls')),
    path('',include('columns_2.urls')),
    path('',include('columns_3.urls')),
    path('',include('columns_4.urls')),
    path('',include('portfolio_image.urls')),
    path('',include('portfolio_detail_2.urls')),
    path('',include('pages.urls')),
    path('',include('shortcodes.urls')),
    path('',include('contact.urls')),
    
    
   
    
    
    
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


