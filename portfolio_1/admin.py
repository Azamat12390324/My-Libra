from django.contrib import admin
from portfolio_1.models import Portfolio_1

@admin.register(Portfolio_1)
class Portfolio_1(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
  

