from django.db import models

class Home_4(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    icons = models.ImageField(upload_to='home_4/=icons', blank=True)


    image = models.ImageField(upload_to='home_4/images', blank=True)
    image_name = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title
    


    class Meta:
        verbose_name = 'Home_4'
        verbose_name_plural = 'Homes_4'

