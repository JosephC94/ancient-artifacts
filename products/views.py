from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def products(request):
    """Displays the products page. Can only be accessed if the user is logged in"""
    return render(request, 'products.html')