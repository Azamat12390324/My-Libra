from django.contrib import admin
from shortcodes.models import Alert_box, Typography


@admin.register(Alert_box)
class Alert_box(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'icons')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Typography)
class Typography(admin.ModelAdmin):
    #list_display = ('title', 'sub_title', 'icons')
    #list_display_links = ('title', 'sub_title')
    list_filter = ('title',)
    
