from django.shortcuts import get_object_or_404
from features.models import Feature

def cart_contents(request):
    """
    Create a session dict of the cart and make it availble to every logged in session
    """
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    feature_count = 0
    for id, quantity in cart.items():
        feature = get_object_or_404(Feature, pk=id)
        total += quantity * feature.price
        feature_count += quantity
        cart_items.append({'id':id, 'quantity':quantity, 'feature':feature})
        
    return {'cart_items':cart_items, 'total':total, 'feature_count':feature_count}