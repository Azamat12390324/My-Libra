from django.db import models

class Alert_box(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='alert_box/image', blank=True)
    slide = models.ImageField(upload_to='alert_box/slide', blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='alert_box/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    icons = models.ImageField(upload_to='alert_box/icons/', blank=True)
    
    
    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Alert_box'
        verbose_name_plural = 'Alert_boxs'

       
class Typography(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='typography/image', blank=True)
    slide = models.ImageField(upload_to='typography/slide', blank=True)
    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='typography/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    
    
    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Typography'
        verbose_name_plural = 'Typographys'

       