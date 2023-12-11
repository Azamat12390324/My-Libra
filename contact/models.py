from django.db import models

class Contact(models.Model):
    icons = models.ImageField(upload_to='with_map/icons/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    adress = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    site = models.URLField(blank=True) 
    site_name = models.CharField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return self.adress
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    
          
    
    
