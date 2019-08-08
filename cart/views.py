from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_cart(request):
    """Route to allow users to view their cart contents"""
    return render(request, "cart.html")