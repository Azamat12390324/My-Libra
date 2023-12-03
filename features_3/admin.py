from django.contrib import admin
from features_3.models import Features_3

@admin.register(Features_3)
class Features_3(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
  
