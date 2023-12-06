from django.contrib import admin
from columns_3.models import Columns_3

@admin.register(Columns_3)
class Columns_3(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
  

