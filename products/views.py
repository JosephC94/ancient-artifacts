from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def all_products(request):
    """Displays the products page. Can only be accessed if the user is logged in"""
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})
    