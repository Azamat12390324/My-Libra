from django.contrib import admin
from pages.models import Testimonials, Faq, Error_404


@admin.register(Testimonials)
class Testimonials(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'icons')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Faq)
class Faq(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'icons')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)
    
@admin.register(Error_404)
class Error_404(admin.ModelAdmin):
    #list_display = ('title', 'sub_title', 'icons')
    #list_display_links = ('title', 'sub_title')
    list_filter = ('title',)




