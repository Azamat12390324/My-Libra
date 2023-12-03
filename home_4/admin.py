from django.contrib import admin
from home_4.models import Home_4


@admin.register(Home_4)
class Home_4(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'image_name')
    list_display_links = ('title', 'image_name')
    list_filter = ('image_name',)
    

