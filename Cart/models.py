from django.db import models
from django.contrib.auth.models import User
from Products.models import Product
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        if self.user:
            return f"{self.user.username} - {self.product.name} ({self.quantity})"
        else:
            return f"کاربر ناشناس - {self.product.name} ({self.quantity})"
            
    def total_price(self):
        """محاسبه مجموع قیمت هر آیتم در سبد خرید."""
        return self.product.price * self.quantity