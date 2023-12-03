from django.contrib import admin
from home_2.models import Home_2

@admin.register(Home_2)
class Home_2(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide', 'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
    


