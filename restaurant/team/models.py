from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "team/")
    designation = models.CharField(max_length=50)
    insta = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'team'
        