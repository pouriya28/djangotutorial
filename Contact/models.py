from django.db import models



# Create your models here.
class Contactform(models.Model):
    name=models.CharField(max_length=100,verbose_name="نام شما")
    email=models.EmailField(verbose_name="ایمیل")
    phone_number=models.CharField(max_length=12,verbose_name="شماره تلفن")
    description=models.TextField(verbose_name="پیام شما")
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
