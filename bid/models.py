from django.db import models
from django.utils import timezone

class Bid(models.Model):
    """A single bid from a signed in user"""
    bid = models.DecimalField(max_digits=9, decimal_places=2)
    bid_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.bid