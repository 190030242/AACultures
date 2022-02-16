from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100,verbose_name="Username")
    CropName = models.CharField(max_length=100, verbose_name="Crop Name")
    image=models.ImageField(upload_to="img/%y",verbose_name="Crop Image")

    Price = models.CharField(max_length=100, verbose_name="Expected Price")
    contact_us = models.CharField(max_length=100,verbose_name="Contact_us")

    def __str__(self):
        return self.caption

class Imagemain(models.Model):
    username=models.CharField(max_length=100 )
    image=models.ImageField(upload_to="img/%y")
    ImageName = models.CharField(max_length=30, blank=False)
    Price = models.IntegerField(blank=False, verbose_name="Expected Price")
    contact_us= models.CharField(max_length=100)
    def __str__(self):
        return self.username