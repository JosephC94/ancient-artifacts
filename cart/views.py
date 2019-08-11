from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """Displays the contents of the cart"""
    
    return render(request, 'cart.html')
    
    
    
    
def adjust_cart(request, id):
    """Allows the user to adjust the cart quantity of a product"""
    
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
    
def add_to_cart(request, id):
    """Allows user to add a specific item to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))
    