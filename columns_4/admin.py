from django.contrib import admin
from columns_4.models import Columns_4

@admin.register(Columns_4)
class Columns_4(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
  



