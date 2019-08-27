from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name
        
class Bid(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='bids')
    bid = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self):
        return self.bid