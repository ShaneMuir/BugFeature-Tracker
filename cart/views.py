from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from features.views import show_all_features
from django.contrib import messages

# Create your views here.
@login_required
def view_cart(request):
    """Route to allow users to view their cart contents"""
    return render(request, "cart.html")
    

@login_required
def add_to_cart(request, id):
    """Add a feature to the cart for upvoting"""
    quantity = int(request.POST.get('quantity'))
    feature_id = request.POST.get('id')
    cart = request.session.get('cart', {})
    for k,v in cart.items():
        if k == feature_id:
            messages.error(request, "Sorry {0}, that feature is already in your cart".format(request.user), extra_tags="alert-primary")
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
    if cart[id] == 0:
        cart.pop(id)
    return redirect(request.META.get('HTTP_REFERER'))
    
   
def remove_from_cart(request, id):
    """Remove a feature from the cart view"""
    feature_id = request.POST.get('id')
    cart = request.session.get('cart', {})
    for k,v in cart.items():
        if feature_id in k:
            cart.pop(k)
            request.session['cart'] = cart
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Sorry {0} , something went wrong.'.format(request.user), extra_tags="alert-primary")
            return redirect(request.META.get('HTTP_REFERER'))