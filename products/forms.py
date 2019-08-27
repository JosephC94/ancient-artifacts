from django import forms
from .models import Bid

class BidForm(forms.ModelForm):
    bid = forms.DecimalField(max_digits=9, decimal_places=2)
    class Meta:
        model = Bid
        fields = ('bid',)