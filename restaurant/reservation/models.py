from django.db import models

# Create your models here.
class reservation(models.Model):
     name = models.CharField(max_length=50)
     email = models.EmailField()
     date = models.DateField(null=True, blank=True)
     time = models.TimeField(null=True, blank=True)
     no_of_people = models.IntegerField()
     specialRequest = models.TextField(null=True)
     
     
     def __str__(self):
         return self.name