from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    def __str__(self):
        return self.product.name
    def subtotal(self):
        return self.quantity*self.product.price

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_items = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=30)
    order_status = models.CharField(max_length=30, default="pending")
    delivery_status = models.CharField(max_length=30, default="pending")
    date_ordered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
#
class Account(models.Model):
    acctnum=models.CharField(max_length=20)
    acctype=models.CharField(max_length=20)
    amount=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    def __str__(self):
        return self.acctnum