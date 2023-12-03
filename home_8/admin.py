from django.contrib import admin
from home_8.models import Home_8


@admin.register(Home_8)
class Home_8(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'icons')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)


