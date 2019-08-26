from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from django.contrib.auth.decorators import login_required



@login_required
def all_products(request):
    """Displays the products page. Can only be accessed if the user is logged in"""
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})