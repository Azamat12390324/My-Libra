from django.db import models

class Home_6(models.Model):
    photo = models.ImageField(upload_to='home_6/images', blank=True)
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)

    picture = models.ImageField(upload_to='home_6/pictures', blank=True)
    picture_about = models.TextField(blank=True)

    icons = models.ImageField(upload_to='home_6/icons', blank=True)


    def __str__(self) -> str:
        return self.title
    


    class Meta:
        verbose_name = 'Home_6'
        verbose_name_plural = 'Homes_6' 
     

