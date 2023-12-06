from django.contrib import admin
from features_4.models import Features_4

@admin.register(Features_4)
class Features_4(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
  
