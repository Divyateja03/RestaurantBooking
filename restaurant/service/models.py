from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    
    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"
        
    def __str__(self):
        return self.name
