from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotelName=models.CharField( max_length=50)
    hotelDescription= models.CharField( max_length=50)
    bookingPrice=models.IntegerField()
    image=models.ImageField(upload_to="image/" ,default="sample_img")
    
    
    
    
    