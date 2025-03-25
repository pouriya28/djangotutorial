from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name="نام")
    description = models.TextField(verbose_name="توضیحات")
    price = models.DecimalField(max_digits=20, decimal_places=0,verbose_name="قیمت")
    image = models.ImageField(upload_to='products/', blank=True, null=True,verbose_name="عکس")
    activ=models.BooleanField(default=True)
        
    def __str__(self):
        return self.name