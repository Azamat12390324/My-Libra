from django.db import models


class Home_3(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='home_3/images', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)
    low_photo = models.ImageField(upload_to='home_3/images', blank=True)



    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Home_3'
        verbose_name_plural = 'Homes_3'



