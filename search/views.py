from django.shortcuts import render
from products.models import Product

def search(request):
    products = Product.objects.filter(name__icontains=request.GET['a'])
    return render(request, 'products.html', {'products': products})
    
    