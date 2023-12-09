from django.db import models

class Portfolio_image(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='portfolio_image/image', blank=True)
    slide = models.ImageField(upload_to='portfolio_image/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='portfolio_image/blogs_images', blank=True)
    time = models.DateField(blank=True)
    name = models.CharField(max_length=255, blank=True)


    icons = models.ImageField(upload_to='portfolio_image/icons/', blank=True)



    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Portfolio_3'
        verbose_name_plural = 'Portfolio_3'


