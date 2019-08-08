from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from features.views import show_all_features

# Create your views here.
@login_required
def view_cart(request):
    """Route to allow users to view their cart contents"""
    return render(request, "cart.html")
    

@login_required
def add_to_cart(request, id):
    """Add a feature to the cart for upvoting"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER'))
    

def increase_cart(request, id):
    """Increase the quantity of the cart_item"""
    cart = request.session.get('cart', {})
    if cart[id]:
        cart[id] += 1
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER'))
    

def decrease_cart(request, id):
    """Decrease the quantity of the cart_item"""
    cart = request.session.get('cart', {})
    if cart[id]:
        cart[id] -= 1
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER'))