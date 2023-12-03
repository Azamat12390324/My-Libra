from django.contrib import admin
from home_5.models import Home_5


@admin.register(Home_5)
class Home_5(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'icons')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

