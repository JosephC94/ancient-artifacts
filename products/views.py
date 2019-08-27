from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product, Bid
from .forms import BidForm
from django.contrib.auth.decorators import login_required



@login_required
def all_products(request):
    """Displays the products page. Can only be accessed if the user is logged in"""
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})
    

def new_bid(request, pk):
    bids = Bid.objects.all()
    product = get_object_or_404(Product, pk=id)
    products = Product.objects.all()
    if request.method=="POST":
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save()
            return redirect('bid_detail', pk=product.id)
    else:
        form = BidForm()
    
    return render(request, 'bid_detail.html', {"form": form, "products": products, 'bids': bids, "product": product})
    
    
def bid_detail(request, pk):
    products = Product.objects.all()
    bids = Bid.objects.all()
    product = get_object_or_404(Product, pk=id)
    
    return render(request, 'bid_detail.html', {"products": products, "bids": bids, "product": product})