from django.contrib import admin
from home_6.models import Home_6


@admin.register(Home_6)
class Home_6(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'icons')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)


