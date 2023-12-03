from django.contrib import admin
from features_1.models import Features_1

@admin.register(Features_1)
class Features_1(admin.ModelAdmin):
    list_display = ('title', 'sub_title',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
    


