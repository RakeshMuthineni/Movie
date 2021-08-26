from django.db import models

# Create your models here.
class Cinima_Info(models.Model):
    Name= models.CharField(max_length=100)
    Hero = models.CharField(max_length=40)
    Heroin = models.CharField(max_length=30)
    Director = models.CharField(max_length=30)
    Budget = models.CharField(max_length=23)
    Desc = models.TextField()
    poster = models.ImageField(upload_to='posters',default='alt.png')



