from django.contrib import admin
from features_2.models import Features_2

@admin.register(Features_2)
class Features_2(admin.ModelAdmin):
    list_display = ('title', 'sub_title',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
    


