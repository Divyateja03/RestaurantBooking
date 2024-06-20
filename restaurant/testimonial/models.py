from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to='testimonial_list/')
    description = models.TextField(null=True)
    
    class Meta:
        verbose_name = "testimonial"
        verbose_name_plural = "testimonials"
        
    def __str__(self):
        return self.name
