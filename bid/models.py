from django.db import models


class Bid(models.Model):
    bid = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __unicode__(self):
        return self.bid