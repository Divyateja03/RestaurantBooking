from django.db import models
from django.utils.text import slugify


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 50)
    Description = models.TextField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null = True)
    servesPeople = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits = 5)
    preparationTime = models.IntegerField()
    image = models.ImageField(upload_to= 'booking/')
    slug = models.SlugField(blank = True, null = True)
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)
        
        
    class Meta:
        verbose_name = "menu"
        verbose_name_plural = "menu"
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
        
