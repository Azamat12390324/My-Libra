from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('title', 'phone', 'email')
    list_display_links = ('title', 'phone', 'email')
    list_filter = ('adress',)
    