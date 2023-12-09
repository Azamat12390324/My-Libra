from django.contrib import admin
from portfolio_image.models import Portfolio_image

@admin.register(Portfolio_image)
class Portfolio_image(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide',  'name')
    list_display_links = ('title', 'name')
    list_filter = ('name',)
  


