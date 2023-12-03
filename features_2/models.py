from django.db import models

class Features_2(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='features_2/image', blank=True)
    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='features_2/blogs_images', blank=True)
    time = models.DateField(blank=True)
    name = models.CharField(max_length=255, blank=True)


    icons = models.ImageField(upload_to='features_2/icons/', blank=True)



    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Features_2'
        verbose_name_plural = 'Features_2'


