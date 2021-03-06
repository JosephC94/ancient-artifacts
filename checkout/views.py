from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
import stripe
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product





stripe.api_key = settings.STRIPE_SECRET

@login_required()



def checkout(request):
    """Displays the checkout depending if the user is signed in or not"""
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)


        print(payment_form.data)
        print(payment_form.errors)
        
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(order=order, product=product, quantity=quantity)
                order_line_item.save()
            
           
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
                
            except stripe.error.CardError as e:
                
                print(str(e))
                
                messages.error(request, "Card declined. Please try again")
            
            
            
            if customer.paid:
                messages.error(request, "Payment has successfully been made")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Failed to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "Payment with that card has been unsuccessful ")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})