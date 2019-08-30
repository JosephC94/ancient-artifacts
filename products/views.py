from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Product, Bid
from .forms import BidForm
from django.contrib.auth.decorators import login_required



@login_required
def all_products(request):
    """Displays the products page. Can only be accessed if the user is logged in"""
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})
    

def product_detail(request, pk):
    """Pulls the detail for a specific product"""
    product = get_object_or_404(Product, pk=pk)
    
    return render(request, 'product_detail.html', {"product": product})
    

    
def place_bid(request, pk=None):
    """Allows user to place a bid on the item they selected"""
    product = get_object_or_404(Product, pk=pk) if pk else None
    
    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.product = product
            bid.save()
            return redirect(bid_detail, pk)
    else:
        form = BidForm(instance=product)
    return render(request, 'bid_form.html', {'form': form})
    
    
    
    
    
def bid_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    bids = Bid.objects.filter(product=product.id).order_by('-bid')
    
    return render(request, 'bid_detail.html', {"bids": bids, "product": product})