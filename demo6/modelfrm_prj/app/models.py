from django.db import models

# Create your models here.
class Fertilizer(models.Model):
    productImage = models.ImageField(upload_to='products/', default="NoPic")
    Ferlilizername = models.CharField(max_length=100, blank=False,verbose_name="Ferlilizer Name")
    cropname = models.CharField(max_length=100, blank=False,verbose_name="Crop-Name")
    soilname = models.CharField(max_length=100, blank=False,verbose_name="Soil-Name")

    Price = models.CharField(max_length=100, blank=False, verbose_name="Expected Price")
    Options = models.CharField(max_length=100, blank=False, verbose_name="Contact Us")

    class Meta:
        db_table = "Fertilizer_table"