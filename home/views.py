from django.shortcuts import render

# Create your views here.
def index(request):
    """Return our landing page on itinal load"""
    return render(request, 'index.html')
    
    
