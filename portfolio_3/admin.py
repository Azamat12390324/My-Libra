from django.contrib import admin
from portfolio_3.models import Portfolio_3

@admin.register(Portfolio_3)
class Portfolio_3(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
  



