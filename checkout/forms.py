from django import forms
from .models import Order





class MakePaymentForm(forms.Form):
    """Order form for checkout page"""

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2050)]

    credit_card_number = forms.CharField(label='Card number', required=False, min_length=15, max_length=16)
    cvv = forms.CharField(label='CVV code', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode','town_or_city', 'street_address1', 'street_address2','county')