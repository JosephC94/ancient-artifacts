from django.shortcuts import render, get_object_or_404, redirect
from .models import Bid
from .forms import BidForm
from products.models import Product
from products.views import all_products

def bid_detail(request, pk):
    bid = get_object_or_404(Bid, pk=pk)
    return render(request, 'bid_detail.html', {'bid': bid})
    
def create_bid(request, pk):
    bid = get_object_or_404(all_products, pk=pk)
    if request.method == "POST":
        form = BidForm(request.POST, request.FILES, instance=bid)
        if form.is_valid():
            bid = form.save()
            return redirect('products.html', {'bid': bid})
    else:
        form = BidForm(instance=bid)
    return render(request, 'createbidform.html', {'form': form})
    