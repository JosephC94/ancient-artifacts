from django.shortcuts import render

# Create your views here.

def products(request):
    """Displays the products page"""
    return render(request, 'products.html')