from django.db import models

class Portfolio_1(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='portfolio_1/image', blank=True)
    slide = models.ImageField(upload_to='portfolio_1/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='portfolio_1/blogs_images', blank=True)
    time = models.DateField(blank=True)
    name = models.CharField(max_length=255, blank=True)


    icons = models.ImageField(upload_to='portfolio_1/icons/', blank=True)



    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Portfolio_1'
        verbose_name_plural = 'Portfolio_1'

      