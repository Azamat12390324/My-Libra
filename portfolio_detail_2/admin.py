from django.contrib import admin
from portfolio_detail_2.models import Portfolio_detail_2

@admin.register(Portfolio_detail_2)
class Portfolio_detail_2(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
  


