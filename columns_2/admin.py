from django.contrib import admin
from columns_2.models import Columns_2

@admin.register(Columns_2)
class Columns_2(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
  


