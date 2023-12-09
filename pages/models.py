from django.db import models

class Testimonials(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='testimonials/image', blank=True)
    slide = models.ImageField(upload_to='testimonials/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='testimonials/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    icons = models.ImageField(upload_to='testimonials/icons/', blank=True)
    
    
    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

        

class Faq(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='faq/image', blank=True)
    slide = models.ImageField(upload_to='faq/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='faq/blogs_images', blank=True)
    time = models.DateField(blank=True)
    name = models.CharField(max_length=255, blank=True)


    icons = models.ImageField(upload_to='faq/icons/', blank=True)
    
    
    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'

        
class Error_404(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='error_404/image', blank=True)
    slide = models.ImageField(upload_to='error_404/slide', blank=True)


    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Error_404'
        verbose_name_plural = 'Errors_404'

        


