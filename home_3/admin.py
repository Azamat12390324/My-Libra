from django.contrib import admin
from .models import Home_3




@admin.register(Home_3)
class Home_3(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'photo', 'low_title')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

    

