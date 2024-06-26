from django.db import models

# Create your models here.



class specialRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "request"
        verbose_name_plural = "requests"